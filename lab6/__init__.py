from dagster import Definitions, load_assets_from_modules
from lab6.crud import sqlite
from lab6.modeling import randomforest

sqlite_assets = load_assets_from_modules([sqlite, randomforest])

defs = Definitions(
    assets=sqlite_assets,
)