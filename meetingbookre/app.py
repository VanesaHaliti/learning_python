from fastapi import FastAPI

from user import User
from database import Database
import uvicorn

app = FastAPI()

Database.initialise(database="postgres", user="postgres", password="admin", host="localhost")


@app.get("/shto")
async def Insert():
    try:

        user = User('Vanesa', 'Kalt', 'adsfghjk')

        user.save_to_db()

        user_from_db = User.load_from_db_by_email('sdisen')

    except Exception:
        return 'Error'
    return 'Query Successful'
