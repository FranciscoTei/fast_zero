from sqlalchemy import select

from fast_zero.models import User


def test_create_user(session):
    user = User(username='Test', email='email@teste.com', password='secret')

    session.add(user)
    session.commit()

    result = session.scalar(select(User).where(User.username == 'Test'))
    assert result.username == 'Test'
    assert result.password == 'secret'
    assert result.id == 1
