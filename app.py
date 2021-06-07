
from collections import namedtuple

# Packages
from fastapi import FastAPI, Cookie, Depends, APIRouter
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

# Routers
from .routers import *


# Startup Handler
def did_startup():
    print("Server Started")

# Shutdown Handler


def did_shutdown():
    print("Server Stopped")


# Instantiate APP
app = FastAPI(
    debug=True,
    title="BluhbergAPI",
    description="",
    version="1.0.0",
    openapi_tags=[],
    on_startup=[did_startup],
    on_shutdown=[did_shutdown]
)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Instantiate Routers
Router = namedtuple('Router', ['router', 'name', 'prefix', 'dependencies'])


ROUTERS = [
    # System Router
    Router(
        router=system_router,   # APIRouter Object ./routers/__init__.py
        name="System",          # Name for Documentation
        prefix="/auth",         # API Prefix
        dependencies=[]         # Dependencies
    ),
    Router(
        router=stonks_router,   # APIRouter Object ./routers/__init__.py
        name="Stonks",          # Name for Documentation
        prefix="/stonks",         # API Prefix
        dependencies=[]         # Dependencies
    ),


    # Example Router
    # Router(router=example_router, name="Example", prefix="/example", dependencies=[]),
]

for router in ROUTERS:
    app.include_router(
        router=router.router,
        prefix=router.prefix,
        tags=[router.name],
        dependencies=router.dependencies
    )

