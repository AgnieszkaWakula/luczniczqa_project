import pytest

from assertpy import assert_that

from tests.libs.config import Config
from tests.libs.crud_methods import create, read


@pytest.fixture
def status():
    response = read(f"{Config.URL}/status/",
                    headers={
                        "accept": "application/json",
                    })
    assert_that(response.status_code).is_equal_to(200)
    return response.json()["data"][0]["status"]

@pytest.fixture
def set_app_status(request):
    payload = {
        "status": request.param["status"]
    }
    response = create(f"{Config.URL}/status/",
                      headers={
                          "accept": "application/json",
                      },
                      json=payload)
    assert_that(response.status_code).is_equal_to(200)
