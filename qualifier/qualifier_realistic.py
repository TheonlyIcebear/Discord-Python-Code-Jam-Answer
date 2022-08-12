import typing, asyncio, random, string
from dataclasses import dataclass


@dataclass(frozen=True)
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
        self.registerWorkers()


    async def __call__(self, request: Request):
        """Handle a request received.
        This is called for each request received by your application.
        In here is where most of the code for your system should go.
        :param request: request object
            Request object containing information about the sent
            request to your application.
        """
        request = request.scope
        if request["type"] == "staff.onduty":
            self.staff[request["id"]] = request

        elif request["type"] == "staff.offduty":
            del self.staff[request["id"]]

        elif request["type"] == "order":
            full_order = await request.recieve()
            speciality_needed = request["speciality"] 
            for worker in self.staff:
                if speciality_needed in worker.scope["speciality"]:
                    worker = worker
                    break
            await worker.send(full_order)

            result = await worker.receive()
            await r.send(result)
