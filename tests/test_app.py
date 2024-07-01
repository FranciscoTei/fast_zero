from http import HTTPStatus

database = []


def test_root_deve_retornar_ok_e_ola_mundo(client):
    response = client.get('/')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'Hello': 'World'}


def test_template_deve_retornar_fastapi(client):
    response = client.get('/template')

    assert response.status_code == HTTPStatus.OK
    assert (
        response.text
        == """<!DOCTYPE html>
    <html>
    <head>
        <title>FastAPI</title>
    </head>
    <body>
        <h1>FastAPI</h1>
    </body>"""
    )


def test_create_user(client):
    response = client.post(
        '/users/',
        json={
            'username': 'Test',
            'email': 'chico@gmail.com',
            'password': 'secret',
        },
    )
    assert response.status_code == HTTPStatus.CREATED
    assert response.json() == {
        'username': 'Test',
        'email': 'chico@gmail.com',
        'id': 1,
    }


def test_read_users(client):
    response = client.get('/users/')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'users': [
            {
                'username': 'Test',
                'email': 'chico@gmail.com',
                'id': 1,
            }
        ]
    }


def test_read_user_especified(client):
    response = client.get('/users/1')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
            'username': 'Test',
            'email': 'chico@gmail.com',
            'id': 1,
        }


def test_update_user(client):
    response = client.put(
        '/users/1',
        json={
            'password': 'secret',
            'username': 'Duno',
            'email': 'duno@ssauro.com',
        },
    )
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'username': 'Duno',
        'email': 'duno@ssauro.com',
        'id': 1,
    }


def test_update_user_not_found(client):
    response = client.put(
        '/users/2',
        json={
            'password': 'secret',
            'username': 'Duno',
            'email': 'duno@ssauro.com',
        },
    )
    assert response.status_code == HTTPStatus.NOT_FOUND
    assert response.json() == {
        'detail': 'User not found',
    }


def test_delete_user(client):
    response = client.delete('/users/1')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'message': 'User deleted'}


def test_delete_user_not_found(client):
    response = client.delete('/users/2')

    assert response.status_code == HTTPStatus.NOT_FOUND
    assert response.json() == {'detail': 'User not found'}
