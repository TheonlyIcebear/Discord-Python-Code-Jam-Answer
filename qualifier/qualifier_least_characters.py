import typing, asyncio, random, string
from dataclasses import dataclass


@dataclass(frozen=False)
class Request:
    scope: typing.Mapping[str, typing.Any]

    receive: typing.Callable[[], typing.Awaitable[object]]
    send: typing.Callable[[object], typing.Awaitable[None]]


class RestaurantManager:
    def __init__(self):
        """Instantiate the restaurant manager.
        This is called at the start of each day before any staff get on
        duty or any orders come in. You should do any setup necessary
        to get the system working before the day starts here; we have
        already defined a staff dictionary.
        """
        self.staff = {}

async def __call__(self, r: Request):
    r.s,r.r,r.e,s,t,p=r.scope,r.receive,r.send,self.staff,"type","speciality";d=r.s
    if d[t]=="staff.onduty":s[d["id"]] = r
    elif d[t]=="staff.offduty":del s[d["id"]]
    elif d[t]=="order":s=s.values();h=[*s][[r.s[p]in w.scope[p]for w in s].index(1)];await h.e(await r.r());await r.e(await h.r())
