from libs.schema import InSchema, OutSchema


class UserResponse(OutSchema):
    id: int
    username: str
    is_admin: bool


class UserIn(InSchema):
    username: str
    password: str
    first_name: str
    last_name: str
    email: str


class UserLogin(InSchema):
    username: str
    password: str
