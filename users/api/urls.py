from django.urls import include, path
from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register(r"", views.UserViewSet)

urlpatterns = router.urls

app_name = "users_api"
