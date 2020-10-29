from abc import ABC, abstractmethod
import enum
from typing import List, Union
from django.urls import path


class ResourceType(enum.Enum):
    CLASS = 1
    FUNCT = 2


class Resource(ABC):
    include: List[str] = ["index", "show"]
    exclude: List[str] = []
    route_type = ResourceType.CLASS
    name: Union[None, str] = None
    url_spec = {"index": "", "show": "<slug:pk>"}

    @property
    @abstractmethod
    def view(self):
        pass

    def __iter__(self):
        return self.__gen_paths()

    def __gen_paths(self):
        merge = set([*self.include, *self.exclude])
        if self.route_type is ResourceType.CLASS:
            for route in merge:
                route_object = f"{self.name.capitalize()}{route.capitalize()}"
                if hasattr(self.view, route_object):
                    yield path(
                        self.url_spec[route],
                        getattr(self.view, route_object).as_view(),
                        name=f"{self.name}_{route}",
                    )
        else:
            pass
