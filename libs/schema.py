from ninja import Schema as NinjaSchema
from .util import to_camel


class InSchema(NinjaSchema):
    """Accepts camelCase paramaters, and creates snake_case equivalents
    this way, the frontend can send their data in camelCase and we can read
    it as snake_case. Allowing both JS and Python language conventions
    """

    class Config(NinjaSchema.Config):
        alias_generator = to_camel


class OutSchema(NinjaSchema):
    """Excepts snake_case paramaters, and outputs camelCase equivelants
    this way, the backend can send their data in snake_case and the frontend
    can read it as camelCase. Allowing both JS and Python language conventions
    """

    def dict(self, **kwargs):
        return {to_camel(key): value for key, value in super().dict(**kwargs).items()}
