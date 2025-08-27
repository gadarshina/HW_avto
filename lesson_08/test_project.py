import pytest
import requests


BASE_URL = "https://ru.yougile.com/api-v2"
HEADERS = {
"Authorization": "Bearer 67BfuLKpWsO9e8HaPw+KybwqiPvck9URIUvS6w+5+pgw6BQg367+HWt1xspbqG5m" ,
"Content-Type": "application/json"
}


@pytest.mark.positive
def test_create_project_success():
    my_project = {
    "title": "Госуслуги"
    }
    response = (requests.post
                (BASE_URL + '/projects',json=my_project, headers=HEADERS))
    assert response.status_code == 201


@pytest.mark.negative
def test_create_project_missing_name():
    data = {
    "user": "Missing name field"
}
    response = requests.post(BASE_URL, json=data, headers=HEADERS)
    assert response.status_code == 404


@pytest.mark.positive
def test_put_project_id():
    my_project = {
        "title": "Госуслуги"
    }
    response = (requests.post
                (BASE_URL + '/projects', json=my_project, headers=HEADERS))
    project_id = response.json().get("id")
    my_project_id = {
    "title": "Change name"
    }
    response = (requests.put
                (f"{BASE_URL}/projects/{project_id}",json=my_project_id, headers=HEADERS))
    assert response.status_code == 200


@pytest.mark.negative
def test_create_negative_get():
   project_id = ""
   url = f"{BASE_URL}/projects/{project_id}"
   response = requests.put(url, headers=HEADERS)
   assert response.status_code == 404

@pytest.mark.negative
def test_put_negative_id():
    project_id = " "
    my_project_id = {
    "title": "ГосУслуги"
}
    response = requests.put(f"{BASE_URL}/projects/{project_id}",
    json=my_project_id, headers=HEADERS)
    assert response.status_code == 404


def test_get_project():
    my_project = {
        "title": "Госуслуги"
    }
    response = (requests.post
                (BASE_URL + '/projects', json=my_project, headers=HEADERS))
    project_id = response.json().get("id")
    url = f"{BASE_URL}/projects/{project_id}"
    response = requests.get(url, headers=HEADERS)
    assert response.status_code == 200