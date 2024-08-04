# from urllib import response
from fastapi import FastAPI
from fastapi.responses import HTMLResponse

from fast_zero.routers import auth, todo, users

app = FastAPI()

app.include_router(users.router)
app.include_router(auth.router)
app.include_router(todo.router)


@app.get('/')
def read_root():
    return {'message': 'World'}


@app.get('/template', response_class=HTMLResponse)
def read_template():
    return """<!DOCTYPE html>
    <html>
    <head>
        <title>FastAPI</title>
    </head>
    <body>
        <h1>FastAPI</h1>
    </body>"""
