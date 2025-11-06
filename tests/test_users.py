from app import schemas
from jose import jwt
from app.config import settings
import pytest


def test_root(client):
    res = client.get("/")
    # print(res.json())
    assert res.json().get('message') == 'Everything in its right place.'
    assert res.status_code == 200
    
def test_create_user(client):
    res = client.post("/users/", json={"email": "stanislaus@gmail.com", "password": "stanislaus"})
    new_user = schemas.UserOut(**res.json())
    assert new_user.email == "stanislaus@gmail.com"
    assert res.status_code == 201
    
def test_login_user(client, test_user):
    res = client.post("/login", data={"username": test_user['email'], "password": test_user['password']})
    login_res = schemas.Token(**res.json())
    
    payload = jwt.decode(login_res.access_token, settings.secret_key, algorithms=[settings.algorithm])
    id = payload.get("user_id")
    
    assert id == test_user['id']
    assert login_res.token_type == 'bearer'
    assert res.status_code == 200

@pytest.mark.parametrize("email, password, status_code", [
    ('stanislaus@gmail.com', 'wrongPassword', 403),
    ('wrongEmail', 'stanislaus', 403),
    ('wrongEmail', 'wrongPassword', 403),
    (None, 'stanislaus', 403),
    ('stanislaus@gmail.com', None, 403)
])
def test_incorrect_login(client, test_user, email, password, status_code):
    res = client.post("/login", data={"username": email, "password": password})
    
    assert res.status_code == status_code
