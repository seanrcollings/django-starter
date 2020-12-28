from typing import List
from pathlib import Path
from importlib import import_module

from django.urls import re_path
from django.shortcuts import render


class PackRoutes:
    CATCH_ALL_REGEX: str = r"(?P<path>.*)$"

    def __init__(self, app_name, base="index"):
        self.app_name = app_name
        self.base = base
        self.urls = self.pack_routes()

    def pack_routes(self):
        """Discovers templates intended for routing the user to a frontend
        application

        The routes packing pipeline will check for a view to associate with
        the template (index.html, views.index). If one is found, it will be used.
        If none is found, a default one will be created to render the template

        :param app_name: The Django app you want to check for templates
        :param base: name of template you want to appear as the base (empty) route
            - defaults to 'index'
        """
        # Does Django provide a way to look inside of installed apps?
        template_path = Path(self.app_name) / f"templates/{self.app_name}"
        self.__assert_path(template_path)
        packs_path = Path(self.app_name) / "packs"
        self.__assert_path(packs_path)

        entry_points: List[Path] = list(template_path.glob("*.html"))

        index = None
        paths = []
        for entry_point in entry_points:
            if entry_point.stem == self.base:
                index = entry_point
            else:
                paths.append(self.__get_path(entry_point.stem, entry_point.name))

        # Have to add the emtpy catch all last
        # or else it will catch routes that should
        # be going to rules below it
        if index:
            paths.append(self.__get_path("", index.name))

        return paths

    def repack(self):
        self.urls = self.pack_routes()
        return self.urls

    def __get_path(self, route, template_name):
        """Returns the Django re_path object used for url matching
        :param route: the routing namespace ('useres', 'goals', 'profile', etc...)
        :param template_name: name of the template that the route should render
        :app_name: Django app to load templates from
        """
        func = self.__get_view_function(route, template_name)
        return re_path(rf"^{route}/{self.CATCH_ALL_REGEX}", func, name=route)

    def __get_view_function(self, func_name, template_name):
        """Checks for a view module with a func that matches the rout
        in the provide app. If one does exist, returns that function
        Elsewise, returns a function that will just render the template
        """
        default_func = lambda request, path, template_name=template_name: render(
            request, f"{self.app_name}/{template_name}"
        )

        try:
            views = import_module(f"{self.app_name}.views")
            if hasattr(views, func_name):
                return getattr(views, func_name)
            return default_func
        except ImportError:
            return default_func

    @staticmethod
    def __assert_path(path: Path):
        if not path.exists():
            raise FileNotFoundError(f"{path.resolve()} does not exist")
        if not path.is_dir():
            raise ValueError(f"{path.resolve()} is not a directory")
