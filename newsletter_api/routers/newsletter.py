from typing import List
from fastapi import APIRouter, Depends
from ..auth import get_user
from ..models.user import User
from ..models.newsletter import Newsletter

# Declare Router
router = APIRouter()


@router.post("/", response_model=Newsletter)
def create(newsletter: Newsletter.IN, user: User = Depends(get_user)):
    """ Create a new newletter """
    return {}


@router.get("/", response_model=List[Newsletter])
def list(user: User = Depends(get_user)):
    """ Lists all newletters of the current User """
    return {}


@router.get("/{newsletter_id}", response_model=Newsletter)
def get(newsletter_id: str, user: User = Depends(get_user)):
    """ Get a specific newsletter """
    return {}


@router.put("/{newsletter_id}", response_model=Newsletter)
def update(newsletter_id: str, newsletter: Newsletter.IN, user: User = Depends(get_user)):
    """ Update a Newsletter """
    return {}


@router.delete("/{newsletter_id}", response_model=Newsletter)
def delete(newsletter_id: str, user: User = Depends(get_user)):
    """ Deletes a specific newletter """
    return {}
