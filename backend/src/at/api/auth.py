import hashlib
import secrets
from datetime import UTC, date, datetime, timedelta

import httpx
from fastapi import APIRouter, Cookie, Depends, Query, Response
from fastapi.responses import HTMLResponse, RedirectResponse
from sqlalchemy.dialects.postgresql import Insert
from sqlalchemy.ext.asyncio import AsyncSession

from at.config import secret
from at.db.base import get_db
from at.db.enums import HCAStatus
from at.db.models import Session, User
from at.schemas.address import Address

router = APIRouter()

SCOPES = "name verification_status slack_id birthdate address basic_info"
STATE_COOKIE = "oauth_state"
SESSION_COOKIE = "session"
SESSION_LIFETIME = timedelta(weeks=2)

@router.get("/test")
async def testrouter():
    response = HTMLResponse(f"""
        <body style="background-color: #121714; margin: 20vh 30vw;">
            <div style="border: 0.4rem solid #FF499E; display: flex; flex-direction: column; align-items: center; justify-content: center;">
            <h1 style="font-family: monospace; color: #FFC60A; font-weight: 800; font-size: 2rem;">
                thank you for signing up for @!!!
            </h1>
            <p style="font-family: monospace; font-size: 1rem; color: #14F5AA;">
                hi!
            </p>
        </body>
    """)
    return response

@router.get("/login")
async def login(email: str):
    state = secrets.token_urlsafe(24)

    params = {
        "client_id": secret().hca_id,
        "redirect_uri": secret().hca_uri,
        "response_type": "code",
        "scope": SCOPES,
        "state": state,
        "login_hint": email
    }
    redirect = RedirectResponse(url=f"https://auth.hackclub.com/oauth/authorize?{httpx.QueryParams(params)}")

    redirect.set_cookie(
        STATE_COOKIE,
        state,
        max_age = 600,
        httponly = True,
        secure = True,
        samesite = "lax",
    )
    return redirect

def _fail(reason: str) -> HTMLResponse:
    return HTMLResponse(
        f"""
        <body style="background-color: #570808; display: flex; flex-direction: column; align-items: center; justify-content: center;">
            <h1 style="padding-top: 20vh; text-align: center; color: #FFC60A; font-family: monospace; font-size: 2rem;">ERROR:</h1>
            <p style="text-align: center; color: #14F5AA; font-family: monospace; font-size: 1.2rem; font-weight: 700;">{reason}</p>
            <p style="text-align: center; color: #14F5AA !important; font-family: monospace; font-size: 1.2rem;"><a href="/">return home</a></p>
        </body>
        """,
        status_code=400)

@router.get("/callback")
async def callback(
    response: Response,
    db: AsyncSession = Depends(get_db),
    code: str | None = Query(default = None),
    state: str | None = Query(default = None),
    oauth_state: str | None = Cookie(default = None, alias=STATE_COOKIE)
):

    if code is None or state is None:
        return _fail("missing code or state from HCA")
    if oauth_state is None or state != oauth_state:
        return _fail("state does not match, possible CSRF?")

    async with httpx.AsyncClient(timeout=10.0) as client:
        try:
            token_res = await client.post(
                "https://auth.hackclub.com/oauth/token",
                json = {
                    "client_id": secret().hca_id,
                    "client_secret": secret().hca_secret,
                    "redirect_uri": secret().hca_uri,
                    "code": code,
                    "grant_type": "authorization_code"
                },
            )
            token_res.raise_for_status()
        except httpx.HTTPError as e:
            return _fail(f"couldn't get HCA or wa rejected: {e}")

        access_token = token_res.json().get("access_token")
        if not access_token:
            return _fail("HCA did not respond with a token")

        try:
            me_res = await client.get(
                "https://auth.hackclub.com/api/v1/me",
                headers = {"Authorization": f"Bearer {access_token}"}
            )
            me_res.raise_for_status()
        except httpx.HTTPError as e:
            return _fail(f"could not get profile from HCA: {e}")

    profile = me_res.json()
    hca_id = profile["identity"]["id"]
    email = profile["identity"]["primary_email"]
    birthday_raw = profile["identity"]["birthday"]
    birthday = date.fromisoformat(birthday_raw) if birthday_raw else None

    if not hca_id or not email:
        return _fail("i couldn't tell who you are!!")

    is_verified = profile["identity"]["verification_status"]
    is_ysws = profile["identity"]["ysws_eligible"]

    if is_verified == "verified" and is_ysws:
        status = HCAStatus.OK
    elif not is_ysws:
        status = HCAStatus.YSWS_BAN
    elif is_verified == "ineligible":
        status = HCAStatus.VERIFY_BAD
    else:
        status = HCAStatus.UNVERIFIED

    user_data = {
        "hca_id": profile["identity"]["id"],
        "email": profile["identity"]["primary_email"],
        "first_name": profile["identity"]["first_name"],
        "last_name": profile["identity"]["last_name"],
        "slack_id": profile["identity"]["slack_id"],
        "birthday": birthday,
        "hca_ok": status,
        "addresses": [
            Address.model_validate(addr).model_dump(mode="json")
            for addr in profile["identity"]["addresses"]
        ]
    }

    statement = Insert(User).values(**user_data)
    update_columns = {
        column.name: statement.excluded[column.name]
        for column in User.__table__.columns
        if column.name not in ("id", "hca_id", "created_at", "banned", "perm_level", "config")
    }

    statement = statement.on_conflict_do_update(
        index_elements=[User.hca_id],
        set_=update_columns,
    ).returning(User)

    result = await db.execute(statement)
    user = result.scalar_one()

    if user.banned:
        await db.rollback()
        return _fail("Account is banned!!")

    match user.hca_ok:
        case "ok":
            pass
        case "ysws_ban":
            return _fail("You are banned from Hack Club YSWSes.")
        case "verify_bad":
            return _fail("Your ID verification is invalid.")
        case "unverified":
            return _fail("Still waiting on your ID verification...")

    raw_token = secrets.token_urlsafe(32)
    token_hash = hashlib.sha256(raw_token.encode()).hexdigest()
    expires_at = datetime.now(UTC) + SESSION_LIFETIME

    db.add(Session(
        token_hash=token_hash,
        user_id=user.id,
        expires_at=expires_at,
    ))
    await db.commit()

    response = HTMLResponse(f"""
        <body style="background-color: #121714; margin: 20vh 30vw;">
            <div style="border: 0.4rem solid #FF499E; display: flex; flex-direction: column; align-items: center; justify-content: center; padding: 0rem 0.6rem;">
            <h1 style="font-family: monospace; color: #FFC60A; font-weight: 800; font-size: 2rem;">
                thank you for signing up for @!!!
            </h1>
            <p style="font-family: monospace; font-size: 1rem; color: #14F5AA;">
                hi {user.first_name}!! Right now, this is just here to demonstrate that authentication works.
                soon, you'll be able to rsvp and actually log into the platform! isn't that awesome!!
            </p>
            <br>
            <p style="font-family: monospace; font-size: 1rem; color: #14F5AA;">
                ty <3
            </p>
        </body>
    """)
    response.set_cookie(
        SESSION_COOKIE,
        raw_token,
        expires=expires_at,
        httponly=True,
        secure=True,
        samesite="lax",
    )
    response.delete_cookie(STATE_COOKIE)
    return response
