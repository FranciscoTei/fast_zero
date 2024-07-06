from http import HTTPStatus


def test_root_deve_retornar_ok_e_ola_mundo(client):
    response = client.get('/')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'message': 'World'}


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
