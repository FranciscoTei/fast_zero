# from urllib import response
from http import HTTPStatus

from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse

from fast_zero.schemas import Message, UserDB, UserList, UserPublic, UserSchema

app = FastAPI()


@app.get('/')
def read_root():
    return {'Hello': 'World'}


database = []


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


@app.get('/database', response_class=HTMLResponse)
def read_database():
    print(database)


@app.post('/users/', status_code=HTTPStatus.CREATED, response_model=UserPublic)
def create_user(user: UserSchema):
    user_with_id = UserDB(id=len(database) + 1, **user.model_dump())
    print(user_with_id)

    database.append(user_with_id)
    print(database[0])
    return user_with_id


@app.get('/users/', response_model=UserList)
def read_users():

    return {'users': database}


@app.get('/users/{user_id}', response_model=UserPublic)
def read_user(user_id: int):

    return database[user_id - 1]


@app.put('/users/{user_id}', response_model=UserPublic)
def update_user(user_id: int, user: UserSchema):

    if user_id < 1 or user_id > len(database):
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND,
            detail='User not found')
    user_with_id = UserDB(id=user_id, **user.model_dump()
        )
    database[user_id - 1] = user_with_id
    return user_with_id


@app.delete('/users/{user_id}', response_model=Message)
def delete_user(user_id: int):
    if user_id < 1 or user_id > len(database):
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND,
            detail='User not found'
        )
    del database[user_id - 1]
    return {'message': 'User deleted'}
