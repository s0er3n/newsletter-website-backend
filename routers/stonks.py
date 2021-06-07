from fastapi import APIRouter
from .stonks_logic import get_history
# Declare Router
router = APIRouter()


# Router Endpoint
@router.get("/hist/{ticker}")
def hist(ticker: str):
    """ get hist of stonk"""


    return get_history(ticker)