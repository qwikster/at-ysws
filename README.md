# @ YSWS
a new Hack Club YSWS (You Ship We Ship)! Uses FastAPI + SQLAlchemy + SvelteKit!

## Hosting locally
> [!NOTE]
> Dockerfile will be added once deployment is ready! For now, this probably shouldn't be used in production. 

### Prerequisites:
git, bun, uv + python, server running Linux, postgresql

```sh
git clone https://github.com/qwikster/at-ysws && cd at-ysws/frontend
bun install && bun run build
cd ../backend
```
- edit `app.config` for your port, and disable `devmode`.
- copy .env.example to .env, add your [HCAuth app keys](https://auth.hackclub.com/docs/tldr)
- create a Postgres server and add it to .env, like:
`postgresql+asyncpg://at:password@server.net.qwik.top:5432/at_dev`

> [!WARNING]
> The database should NOT be exposed to the Internet.

- ensure your backend port is exposed to the internet, then:
```sh
uv sync && uv venv
source .venv/bin/activate
uv run at-run
```
Server should be up!

## Development
Assumes you've already gone through the [steps](#hosting-locally) above. Make sure you've also installed Ruff and Pyright for type hinting.
- Turn on `devmode` in /backend/app.config
- Run SvelteKit's dev server alone:
```sh
bun run dev --open
```
- Run the backend with `uv run at-run`
- Wipe the database if needed with `uv run at-drop` and reload the backend

You can also message @qwik on Slack if you need help :)

## AI Usage
Some AI was used for planning and debugging. **No code** was directly written by AI. Slop PRs will be rejected if you clearly don't understand the additions you've made.

## Contributing
you're welcome to make additions to @! best to contact me on Slack before you start working on a large feature, though, to stop you wasting time :)   if you have any other suggestions but don't want to implement them (fairs), contact me for them too!
