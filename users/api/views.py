from typing import List
from django.contrib.auth import authenticate, login
from ninja import Router
from ninja.security import django_auth

from libs.util import error

from ..forms import RegistrationForm, LoginForm
from ..models import User
from .schemas import *

router = Router()


@router.get("/", response=List[UserResponse])
def list_users(request):
    return User.objects.all()


@router.post("/", response=UserResponse)
def create_user(request, payload: UserIn):
    form = RegistrationForm(payload.dict())
    if form.is_valid():
        user = User(**payload.dict())
        user.save()
        return user

    return error(form.errors)


@router.post("/login/", response=UserResponse)
def login_user(request, payload: UserLogin):
    form = LoginForm(payload.dict())
    if form.is_valid():
        user = authenticate(request, **payload.dict())
        if user is not None:
            login(request, user)
            return user

        return error({"detail": "Username or password is incorrect"})

    return error(form.errors)
