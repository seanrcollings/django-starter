from typing import List, Dict
from io import StringIO

from django.core.management.base import BaseCommand
from django.core.management import call_command
from libs.util import safe_unpack


class Command(BaseCommand):
    help = "Wrapper around django_extensions show_url to provide better formatting and various options"

    def add_arguments(self, parser):
        parser.add_argument(
            "-f",
            "--filter",
            help="Filter urls to contain the provided string",
        )
        parser.add_argument(
            "-nf",
            "--no-format",
            action="store_true",
            default=False,
            help="Disable the special formatting",
        )

    def handle(self, *args, **options):
        out = StringIO()
        call_command("show_urls", stdout=out)
        routes = out.getvalue().split("\n")
        urls: List[Dict[str, str]] = []
        for route in routes:
            url, method, name, _ = safe_unpack(route.split("\t"), 4, "")
            show = not (options["filter"] and not options["filter"] in url)
            if show:
                urls.append({"url": url, "method": method, "name": name})

        keyfunc = lambda x: len(repr(x))
        url_width = len(max([url["url"] for url in urls], key=keyfunc)) + 5
        method_width = len(max([url["method"] for url in urls], key=keyfunc)) + 5
        name_width = len(max([url["name"] for url in urls], key=keyfunc)) + 5

        for url in urls:
            url, method, name = url.values()
            if options["no_format"]:
                self.stdout.write(f"{url}     {method}     {name}")
            else:
                self.stdout.write(
                    (
                        f"{url:<{url_width}}"
                        f"{method:<{method_width}}"
                        f"{name:<{name_width}}"
                    )
                )
