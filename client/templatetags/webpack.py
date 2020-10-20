from django import template
from django.conf import settings
from django.templatetags.static import static

register = template.Library()


@register.simple_tag
def assets(pack: str) -> str:
    if settings.ENVIRONMENT == "development":
        return f"{settings.WEBPACK_ROOT_URL}/static/{pack}.js"
    else:
        return static(f"client/js/{pack}.js")