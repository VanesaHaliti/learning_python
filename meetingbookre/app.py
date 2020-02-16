from fastapi import FastAPI

from user import User
from database import Database
import uvicorn

app = FastAPI()

Database.initialise(database="postgres", user="postgres", password="admin", host="localhost")


@app.post("/insert")
async def insert_users():
    try:

        user = User('Stephen@gmail.com', 'Stephen', 'Hawking')

        user.save_to_db()

        user_from_db = User.load_from_db_by_email('blaaaa')

    except Exception:
        return 'Error'
    return 'Query Successful'



