from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import redis
from databases import Database
from api import api
from core import config, connections

app = FastAPI()

origins = [
    'http://localhost:3000',
    'localhost:3000',
]

app.add_middleware(
    CORSMiddleware,
    allow_origins = origins,
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*']
)

app.include_router(router=api.router)

db_postgres = Database(url=config.POSTGRES_URL)


@app.on_event("startup")
async def startup():
    await db_postgres.connect()
    r = redis.Redis(host=config.REDIS_HOST, port=config.REDIS_PORT, db=0, decode_responses=True)
    connections.inject_db(app, db_postgres, r)


@app.on_event("shutdown")
async def shutdown():
    await db_postgres.disconnect()
