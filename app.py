import uvicorn
from collections import namedtuple

# Packages
from fastapi import FastAPI, Cookie, Depends, APIRouter
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

# Routers

from routers.system import router as system
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
        router=system,   # APIRouter Object ./routers/__init__.py
        name="System",          # Name for Documentation
        prefix="/auth",         # API Prefix
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

uvicorn.run(app, host="0.0.0.0", port=8000)
