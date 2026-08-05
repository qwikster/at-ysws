# table layouts

## User
id: int (primary) (index)
created_at: datetime
banned: bool
hca_ok: str # ok | ysws_ban | verify_bad | unverified

### info from hcauth, discard oauth, refresh on login
hca_id: str # PRIMARY for identification
email: str
slack_id: str
username: str null (needs slack bot token and slack api is hell, probably use first_name)
pfp_url: str null (same as above, probably don't use)
first_name: str
last_name: str
birthday: date
addresses: Array[{id, primary, first_name, last_name, line_1, line_2, city, state, postal_code, country, phone}]

permissions: str (user | review | admin)
projects: array[Project] [RELATIONSHIP]
currency: int
hours: float
reviews: array[Review] [RELATIONSHIP]
shop_goals: array[Prize.id] 
shop_orders: array[Order] [RELATIONSHIP] # per user orders
achievements: array[Achievement] [RELATIONSHIP]
liked_projects: array[ProjectLike] [RELATIONSHIP]
config: json

## Project
id: int (primary) (index)
user_id: int
created_at: datetime
name: str
description: str
ai_usage: str
image_url: str
demo: str
repo: str
readme: str
hackatime: array
hours: float
value: int
status: str
shipped_at: datetime null
approved_at: datetime null
reviews: array[Review] [RELATIONSHIP]
likes: array[ProjectLike] [RELATIONSHIP]

## Prize
id: int (primary) (index)
hidden: bool
name: str
description: str
price: json {global: str}
price_hq: float # price to buy for hq
available_regions: array null
stock: int or -1
orders: array[Order] [RELATIONSHIP] # PRIVATE, do not return from GET /api/prizes

## Order
id: int (primary) (index)
user: int[User.id] [RELATIONSHIP]
item: int[Prize.id] [RELATIONSHIP]
status: str # ordered, refunded, shipped, delivered, complete
cost: int
rate: int (cost to hq per hour)
address: json like User.addresses
shipped_at: datetime
delivered_at: datetime

## ProjectLike (optional)
id: int (primary) (index)
project: int[Project.id] [RELATIONSHIP]
user: int[User.id] [RELATIONSHIP]
time: datetime

## Review
id: int (primary) (index)
user: int[User.id] [RELATIONSHIP]
project: int[Project.id] [RELATIONSHIP]
time: datetime
status: str # accept | resubmit | reject (fraud)
feedback: str

## Achievement (optional)
id: int (primary) (index)
type: str from a list
user: int[User.id] [RELATIONSHIP]
time: datetime

## Session
id: int (primary)
token_hash: str (unique) (index) # SHA256 of secrets.token_urlsafe(32)
user_id: int[User.id] [RELATIONSHIP]
created_at: datetime
expires_at: datetime
user_agent: str null
ip: str null
