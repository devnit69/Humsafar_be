from fastapi import FastAPI
import json
from .routers import auth


app = FastAPI()



@app.get('/')
def root():
    return {'response' : 'working'}


app.include_router(auth.router)


