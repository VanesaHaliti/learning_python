from fastapi import FastAPI
from user import User
from pydantic import BaseModel
import uvicorn
from database import Database

app = FastAPI()
Database.initialise(database="postgres", user="postgres", password="admin", host="localhost")
''''
class UserInDB(User):
    id: int
@app.post("/user", response_model=UserInDB)  # we create the user api
def create_user(user: User):
    """This is the roooot"""
    if user.name.lower() == "bill":
        raise ValueError("User cannot be name Bill!")
    return UserInDB(id=1, **user.dict())  # we are unpacking a dictionary into arguments'''


@app.put("/users")
async def user():
    user = User('vaaaaanesa', 'Jose', 'Salvatierra')
    user.save_to_db()
    user_from_db = User.load_from_db_by_email('jose@schoolofcode.me')
    return user


@app.get("/users_from_db")
async def get_user():
    user_from_db = User.load_from_db_by_email('jose@schoolofcode.me')
    return user_from_db




'''@app.post("/user", response_model=User)  # response says give us a user model and it will
async def create_user(user: User):
    """This is the root"""
    if user.name.lower() == 'bill':
        raise ValueError("User cannot be named bill")
    return UserInDB(id=1, **user.dict())  # te ** user.dict() means we are unpacking a dictionary. ** means unpacking


@app.put("/user/{id_number}", response_model=User)  # response says give us a user model and it will
async def update_user(id_number: int, user: User):
    """This is the root"""
    return UserInDB(id=id_number, **user.dict())


@app.get("/users/{user_id}")
async def read_user(user_id):
    return {"user_id": user_id}


@app.delete("/users/{user_id}")
async def delete_user(user_id):
    cur.execute("DELETE FROM user WHERE id_number =%s, user_id")
    deleted_rows = cur.rowcount
    cur.commit()
    con.close()
    return deleted_rows


def test_create_user():  # it takes the User object and turn it into a database user object
    address = Address(street="somestreet")
    user = User(email="abc", name="bill", address=address)
    user_in_db = UserInDB(id=1, **user.dict())
    assert create_user(user) == user_in_db
    assert create_user(user).id == 2  # it fails because id is 1 and we're checking for 2
    # assert create_user(user).id is int
    assert type(create_user(user).id) is int
'''
