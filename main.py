from fastapi import  FastAPI
import random


app=FastAPI()

@app.get('/')
aysnc def root():
    return {'example':'This is an example','data':0}
