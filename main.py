import psycopg2
import os
from os.path import join, dirname
from dotenv import load_dotenv
from fastapi import FastAPI
dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)
load_dotenv()


from routers import users, transactions

app = FastAPI()

app.include_router(users.router)
app.include_router(transactions.router)

@app.get('/')
def hello():
    return {"Hello": "World"}


conn = psycopg2.connect(
    database=os.environ.get("DB"),
    host=os.environ.get("PSQL_HOST"),
    user=os.environ.get("PSQL_USERNAME"),
    password=os.environ.get("PSQL_PASSWORD"),
    port=os.environ.get("PSQL_PORT"),
)

cursor = conn.cursor()



