from django.urls import path, re_path

from . import views

catch_all: str = r"(?P<path>.*)"

urlpatterns = [re_path(r"test/" + catch_all, views.index), path("other", views.other)]
