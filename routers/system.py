from fastapi import APIRouter


# Declare Router
router = APIRouter()


# Router Endpoint
@router.get("/test")
def test():
    """ This is a Test-Endpoint """
    res = {
        'message': 'Hello World!'
    }

    return res
