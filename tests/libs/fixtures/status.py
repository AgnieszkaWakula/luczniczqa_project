import pytest

from assertpy import assert_that

from tests.libs.config import Config
from tests.libs.crud_methods import read


@pytest.fixture
def status():
    response = read(f"{Config.URL}/status/",
                    headers={
                        "accept": "application/json",
                    })
    assert_that(response.status_code).is_equal_to(200)
    return response.json()["data"][0]["status"]
