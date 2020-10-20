from django.urls import path

from . import views

urlpatterns = [
    path("", views.UsersList.as_view(), name="users_index"),
    path("login", views.LoginView.as_view(), name="login"),
    path("logout", views.logout_view, name="logout"),
]