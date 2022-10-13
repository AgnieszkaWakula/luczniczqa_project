import pytest
import requests
from assertpy import assert_that, soft_assertions


@pytest.mark.admin
class TestAnyEndpoint:
    def test_01_get_root_response_200(self):
        response = requests.get("http://127.0.0.1:8080/",
                                headers={
                                    "accept": "application/json",
                                    "Content-Type": "application/json"
                                })
        with soft_assertions():
            assert_that(response.status_code).is_equal_to(201)
            print("assert_1")
            # assert response.status_code == 200
            print("assert_2")
            assert_that(response.json()["message"]).contains("API Testing app")
            # assert response.json()['message'] == 'Welcome to EGNYTE API Testing app.'

    def test_02_simple_test(self):
        print("Hello I am second test")
