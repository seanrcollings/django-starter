from ninja import Schema

from libs.schema import SchemaEx


class UserResponse(Schema):
    id: int
    username: str
    is_admin: bool


class UserIn(SchemaEx):
    username: str
    password: str
    first_name: str
    last_name: str
    email: str


class UserLogin(SchemaEx):
    username: str
    password: str