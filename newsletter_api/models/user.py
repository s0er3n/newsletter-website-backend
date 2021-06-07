from pydantic import BaseModel, EmailStr


class User(BaseModel):
    id: str
    email: EmailStr

    @staticmethod
    def default():
        """ Default User for Development """
        return User(id="NONE", email="user@email.com")
