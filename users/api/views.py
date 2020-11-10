from typing import List
from ninja import Router
from libs.util import error
from ..forms import RegistrationForm
from ..models import User

from .schemas import UserResponse, UserIn

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
