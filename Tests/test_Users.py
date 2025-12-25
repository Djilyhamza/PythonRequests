import pytest
from Utils.apis import API
from conftest import load_user_data
import os
import uuid


@pytest.fixture(scope="module")
def apis():
    return API()


def test_get_user_validation(apis):
    response = apis.get("users")
    assert response.status_code == 200

def test_post_user(apis, load_user_data):
    test_data = load_user_data
    unique_email = f"{uuid.uuid4().hex[:8]}@gmail.com"
    test_data["email"] = unique_email
    response = apis.post("users", test_data)
    print(response.json())
    assert response.status_code == 201
    # Step 3: GET the user by ID
    get_response = apis.get(f"users/10")
    assert get_response.status_code == 200  # check GET succeeded


def test_update_user(apis):
    # Step 1: POST a new user
    data_user = {"name": "boby", "username": "chiwawa", "password": "1223234"}
    put_response = apis.put("users/10", data_user)
    assert put_response.status_code == 200
    assert put_response.json()["name"] == "boby"


def test_delete_user(apis):
    delete_response = apis.delete("users/10")
    assert delete_response.status_code == 200
    print(delete_response.json())











