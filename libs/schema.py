from ninja import Schema as NinjaSchema


class SchemaEx(NinjaSchema):
    """My custom Schema
    - Camel Case serilzation
    """

    def __init__(self, *args, **kwargs):
        # pretty uggo lol
        super().__init__(
            *args,
            **{
                snake_key: val
                for key, val in kwargs.items()
                if (
                    snake_key := "".join(
                        ["_" + char.lower() if char.isupper() else char for char in key]
                    )
                )
                in self.schema()["properties"]
            },
        )
