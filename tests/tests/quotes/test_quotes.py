import pytest

import requests

from assertpy import assert_that, soft_assertions

@pytest.mark.quote
class TestQuotesEndpoint:
    def test_01_get_list_of_quotes_response_200(self):
        quotes_list = requests.get("http://127.0.0.1:8080/quote/",
                                headers = {
                                    "accept": "application/json",
                                    "Content - Type": "application/json"
                                })
        with soft_assertions():
            #Verify status code
            assert_that(quotes_list.status_code).is_equal_to(200)
            #Verify headers
            # TODO: Do it!
            assert_that(quotes_list.json()["data"][0]).contains(quote_id)
            assert_that(quotes_list.json()["data"][0][0]).contains_key("author")
            assert_that()