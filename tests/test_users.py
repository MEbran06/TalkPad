from app import schemas
from app.routers.auth import login
import pytest
from jose import jwt
from app.config import settings


def test_create_user(client):
    res = client.post(
        "/users/", json={"email": "user1@gmail.com", "password": "password123", "username": "user1"})
    

    new_user = schemas.UserOut(**res.json())
    assert new_user.email == "user1@gmail.com"
    assert res.status_code == 201

def test_login_user(client, test_user):
    res = client.post(
            "/login", data={"email": test_user['email'], "password": test_user['password'], "username": test_user['username']})
    login_res = schemas.Token(**res.json())
    payload = jwt.decode(login_res.access_token, settings.secret_key, algorithms=[settings.algorithm])
    id = payload.get("user_id")
    assert id == test_user['id']
    assert login_res.token_type == 'bearer'
    assert res.status_code == 200

@pytest.mark.parametrize('email, password, status_code, username', [
    ('user1@gmail.com', 'WrongPassword ', 403, 'user1'),
    ('user1@gmail.com', 'password123', 403, 'WrongUsername'),
    ('Wrongemail@gmail.com', 'password123', 403, 'WrongUsername'),
    ('Wrongemail@gmail.com', 'WrongPassword', 403, 'user1'),
    ('user1@gmail.com', 'WrongPassword', 403, 'WrongUsername'),
    ('user1@gmail.com', None, 422, 'user1'),
    ('user1@gmail.com', 'password123', 422, None)

])
def test_incorrect_login(test_user, client, email, password, status_code, username):
    res = client.post("/login", data={"email": email, "password": 
                        password, "username": username})
    
    assert res.status_code == status_code
    #assert res.json().get('detail') == 'Invalid Credentials'