from dagster import load_assets_from_modules, repository

from . import assets


@repository
def lab6():
    return [load_assets_from_modules([assets])]
