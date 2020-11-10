from typing import List
from pathlib import Path
from django.urls import re_path
from django.shortcuts import render


def __assert_path(path: Path):
    if not path.exists():
        raise FileNotFoundError(f"{path.resolve()} does not exist")
    if not path.is_dir():
        raise ValueError(f"{path.resolve()} is not a directory")


def __get_path_obj(stem, name, app_name):
    catch_all: str = r"(?P<path>.*)"
    return re_path(
        rf"{stem}{catch_all}",
        lambda request, path, name=name: render(request, f"{app_name}/{name}"),
        name=stem,
    )


def pack_routes(app_name, base="index"):
    """Discovers templates intended for routing the user to a frontend
    application

    :param app_name: The Django app you want to check for templates
    :param base: name of templat you want to appear as the base (empty) route
        - defaults to 'index'
    """
    # Does Django provide a way to look inside of installed apps?
    template_path = Path(app_name) / f"templates/{app_name}"
    __assert_path(template_path)
    packs_path = Path(app_name) / "packs"
    __assert_path(packs_path)

    entry_points: List[Path] = list(template_path.glob("*.html"))
    pack_names: List[Path] = [
        pack.stem
        for pack in list(packs_path.glob("*.js")) + list(packs_path.glob("*.ts"))
    ]

    index = None
    paths = []
    for entry_point in entry_points:
        assert (
            entry_point.stem in pack_names
        ), f"Template {entry_point} does not have an associated pack"

        if entry_point.stem == base:
            index = entry_point
            continue

        paths.append(__get_path_obj(entry_point.stem, entry_point.name, app_name))

    if index:
        paths.append(__get_path_obj("", index.name, app_name))

    return paths
