import pytest
import requests

from assertpy import assert_that, soft_assertions


@pytest.mark.two
class TestAll:

    def test_01(self):
            response = requests.get("http://127.0.0.1:8080/",
                                    headers={
                                        "accept": "application/json",
                                        "Content-Type": "application/json"
                                    })

            with soft_assertions():
                print("I am checking 1st assertion")
                assert_that(response.status_code).is_equal_to(200)
                print("I am checking 2nd assertion")
                assert_that(response.json()["message"]).is_equal_to("Welcome to EGNYTE API Testing app.")


    def test_02(self):
        response = requests.get("http://127.0.0.1:8080/",
                                headers={
                                    "accept": "application/json",
                                    "Content-Type": "application/json"
                                })

        with soft_assertions():
            print("I am checking 1st assertion")
            assert_that(response.status_code).is_equal_to(201)
            print("I am checking 2nd assertion")
            assert_that(response.json()["message"]).contains("123")


    def test_03(self):
        pass