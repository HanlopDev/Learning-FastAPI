from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def index():
    return {'data':{'name':'home'}}

@app.get('/about')
def about():
    return {'data':"aboute-page"}