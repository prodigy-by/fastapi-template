from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import api 

app = FastAPI()

origins = [
    'http://localhost:5173',
    'localhost:5173',
]

app.add_middleware(
    CORSMiddleware,
    allow_origins = origins,
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*']
)

app.mount('/api', api.app)

@app.get('/ping')
async def ping():
    return {'message':'pong'}

