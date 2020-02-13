from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI()


class Address(BaseModel):  # We create a data transfer object because its more complex
    street: str


class User(BaseModel):
    email: str
    name: str
    id_number: Optional[str]
    address: Address


class UserInDB(User):
    id: int


@app.post("/user", response_model=User)  # response says give us a user model and it will
def create_user(user: User):
    """This is the root"""
    if user.name.lower() == 'bill':
        raise ValueError("User cannot be named bill")
    return UserInDB(id=1, **user.dict())  # te ** user.dict() means we are unpacking a dictionary. ** means unpacking


@app.put("/user/{id_number}", response_model=User)  # response says give us a user model and it will
def update_user(id_number: int, user: User):
    """This is the root"""
    return UserInDB(id=id_number, **user.dict())


@app.get("/user/{user_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}


def test_create_user():  # it takes the User object and turn it into a database user object
    address = Address(street="somestreet")
    user = User(email="abc", name="bill", address=address)
    user_in_db = UserInDB(id=1, **user.dict())
    assert create_user(user) == user_in_db
    assert create_user(user).id == 2  # it fails because id is 1 and we're checking for 2
    # assert create_user(user).id is int
    assert type(create_user(user).id) is int
