from os import environ
from newsletter_api.models.newsletter import Newsletter
from collections import namedtuple

# Packages
from fastapi import FastAPI, Cookie, Depends, APIRouter
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from .routers import system, newsletter

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
        router=system.router,   # APIRouter Object ./routers/__init__.py
        name="System",          # Name for Documentation
        prefix="/auth",         # API Prefix
        dependencies=[]         # Dependencies
    ),
    Router(
        router=newsletter.router,   # APIRouter Object ./routers/__init__.py
        name="Newsletter",          # Name for Documentation
        prefix="/newsletter",         # API Prefix
        dependencies=[]         # Dependencies
    )

]

for router in ROUTERS:
    app.include_router(
        router=router.router,
        prefix=router.prefix,
        tags=[router.name],
        dependencies=router.dependencies
    )

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
