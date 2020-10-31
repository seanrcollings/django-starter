import sys
from typing import List, Any, Sized, Dict
from io import StringIO

from django.core.management.base import BaseCommand, CommandError
from django.core.management import call_command
from libs.util import safe_unpack


class Command(BaseCommand):
    help = "Wrapper around django_extensions show_url to provide better formatting and various options"

    def add_arguments(self, parser):
        parser.add_argument("-f", "--filter")

    def handle(self, *args, **options):
        out = StringIO()
        call_command("show_urls", stdout=out)
        routes = out.getvalue().split("\n")
        urls: List[Dict[str, str]] = []
        for route in routes:
            url, method, name = safe_unpack(route.split("\t"), 3, "")
            show = False if options["filter"] and not options["filter"] in url else True
            if show:
                urls.append({"url": url, "method": method, "name": name})

        keyfunc = lambda x: len(repr(x))
        url_width = len(max([url["url"] for url in urls], key=keyfunc)) + 5
        method_width = len(max([url["method"] for url in urls], key=keyfunc)) + 5
        name_width = len(max([url["name"] for url in urls], key=keyfunc)) + 5

        for url in urls:
            url, method, name = url.values()
            self.stdout.write(
                (
                    f"{url:<{url_width}}"
                    f"{method:<{method_width}}"
                    f"{name:<{name_width}}"
                )
            )
