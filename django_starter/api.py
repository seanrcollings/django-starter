from ninja import NinjaAPI
from users.api.urls import router as users_router

api = NinjaAPI(csrf=True)

api.add_router("/users/", users_router)


@api.get("/hello")
def hello(request):
    return {"key": "value"}
