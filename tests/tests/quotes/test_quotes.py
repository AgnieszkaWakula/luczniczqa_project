from datetime import timedelta

import pytest
import requests

from assertpy import assert_that, soft_assertions


@pytest.mark.quote
@pytest.mark.usefixtures("create_and_delete_quote")
class TestQuotesEndpoint:
    # GET positive - 200
    def test_01_get_list_of_quotes_response_200(self, create_and_delete_quote):
        quotes_list = requests.get("http://127.0.0.1:8080/quote/",
                                   headers={
                                       "accept": "application/json",
                                       "Content - Type": "application/json"
                                   })
        with soft_assertions():
            # Verify status code
            assert_that(quotes_list.status_code).is_equal_to(200)
            # Verify response payload
            assert_that(quotes_list.json()["data"][0][0]).contains("id")
            assert_that(quotes_list.json()["data"][0][0]).contains("quote")
            assert_that(quotes_list.json()["data"][0][0]).contains_key("author")
            assert_that(quotes_list.json()["message"]).is_equal_to("Quotes data retrieved successfully")
            # Verify headers
            assert_that(quotes_list.headers["content-type"]).is_equal_to("application/json")
            assert_that(quotes_list.headers["x-egnyte"]).is_not_empty()
            assert_that(quotes_list.headers["server"]).is_equal_to("uvicorn")
            # Verify basic performance sanity
            assert_that(quotes_list.elapsed).is_less_than_or_equal_to(timedelta(milliseconds=500))

    # POST positive - 200
    def test_02_post_quote_response_response_200(self):
        response = requests.post("http://127.0.0.1:8080/quote/",
                                 headers={
                                     "accept": "application/json"
                                 },
                                 json={
                                     "quote": "In the end, it's not the years in your life that count. It's the life "
                                              "in your years.",
                                     "author": "Abraham Lincoln"
                                 })
        with soft_assertions():
            assert_that(response.status_code).is_equal_to(200)
            # Verify Headers
            assert_that(response.headers["content-type"]).is_equal_to("application/json")
            assert_that(response.headers["server"]).is_equal_to("uvicorn")
            assert_that(response.headers["x-egnyte"]).is_not_empty()
            # Verify Response body!
            assert_that(response.json()["data"][0]).contains_key("id")
            assert_that(response.json()["data"][0]).contains_key("quote")
            assert_that(response.json()["data"][0]).contains_key("author")
            assert_that(response.json()["message"]).is_equal_to("Quote added successfully.")
            # Verify basic performance sanity
            assert_that(response.elapsed).is_less_than_or_equal_to(timedelta(milliseconds=500))

    # POST nad GET with id - 200
    def test_03_get_quote_with_id_response_200(self):
        # Create first, get second
        create_quote = requests.post("http://127.0.0.1:8080/quote/",
                                     headers={
                                         "accept": "application/json",
                                         "Content-Type": "application/json"
                                     },
                                     json={
                                         "quote": "Life is really simple, but we insist on making it complicated.",
                                         "author": "Abraham Lincoln"
                                     })
        # get created quote it:
        quote_id = create_quote.json()["data"][0]["id"]
        get_quote_with_id = requests.get(f"http://127.0.0.1:8080/quote/{quote_id}",
                                         headers={"accept": "application/json"})
        with soft_assertions():
            assert_that(get_quote_with_id.status_code).is_equal_to(200)
            # assert everything
            #Verify Headers
            assert_that(get_quote_with_id.headers["content-type"]).is_equal_to("application/json")
            assert_that(get_quote_with_id.headers["server"]).is_equal_to("uvicorn")
            assert_that(get_quote_with_id.headers["x-egnyte"]).is_not_empty()
            # validate data
            assert_that(get_quote_with_id.json()["data"][0]).contains_key("id")
            assert_that(get_quote_with_id.json()["data"][0]).contains_key("quote")
            assert_that(get_quote_with_id.json()["data"][0]).contains_key("author")
            assert_that(get_quote_with_id.json()["code"]).is_equal_to(200)
            assert_that(get_quote_with_id.json()["message"]).is_equal_to("Quote data retrieved successfully")

    # PUT and GET with id -200
    def test_04_put_quote_with_id_response_200(self):
        # Create first, update second, get updated quote
        create_quote = requests.post("http://127.0.0.1:8080/quote/",
                                     headers={
                                         "accept": "application/json",
                                         "Content-Type": "application/json"
                                     },
                                     json={
                                         "quote": "I never dreamed about success, I worked for it.",
                                         "author": "Estee Lauder"
                                     })
        # get created quote it:
        quote_id = create_quote.json()["data"][0]["id"]
        # PUT - update quote
        update_quote_with_id = requests.put(f"http://127.0.0.1:8080/quote/{quote_id}",
                                            headers={
                                                "accept": "application/json",
                                                "Content-Type": "application/json"
                                            },
                                            json={
                                            "quote": "You’ve got to get up every morning with determination if you’re "
                                                     "going to go to bed with satisfaction.",
                                            "author": "George Lorimer."
                                            })
        with soft_assertions():
            assert_that(create_quote.status_code).is_equal_to(200)
            assert_that(update_quote_with_id.status_code).is_equal_to(200)
            # assert everything
            assert_that(update_quote_with_id.json()["data"][0]).contains("update is successful")
            assert_that(update_quote_with_id.json()["message"]).is_equal_to("Quote updated successfully")
            assert_that(update_quote_with_id.headers["content-type"]).is_equal_to("application/json")
            assert_that(update_quote_with_id.headers["server"]).is_equal_to("uvicorn")
            assert_that(update_quote_with_id.headers["x-egnyte"]).is_not_empty()
            # Verify basic performance sanity
            assert_that(update_quote_with_id.elapsed).is_less_than_or_equal_to(timedelta(milliseconds=500))

    # POST + DELETE with id + GET - 404
    def test_05_delete_quote_with_id_response_200(self):
        # Create first, delete second, verify 404 status code when trying to get quote with id again
        create_quote = requests.post("http://127.0.0.1:8080/quote/",
                                     headers={
                                         "accept": "application/json",
                                         "Content-Type": "application/json"
                                     },
                                     json={
                                         "quote": "If you get tired, learn to rest, not to quit.",
                                         "author": "Banksy"
                                     })
        # get created quote it:
        quote_id = create_quote.json()["data"][0]["id"]
        delete_quote = requests.delete(f"http://127.0.0.1:8080/quote/{quote_id}",
                                       headers={"accept": "application/json"})
        get_quote_with_id = requests.get(f"http://127.0.0.1:8080/quote/{quote_id}",
                                         headers={"accept": "application/json"})
        with soft_assertions():
            assert_that(create_quote.status_code).is_equal_to(200)
            assert_that(delete_quote.status_code).is_equal_to(200)
            assert_that(get_quote_with_id.status_code).is_equal_to(404)
            # assert create
            # assert delete
            assert_that(delete_quote.json()["data"][0]).is_equal_to(f"Quote with ID: {quote_id} removed")
            assert_that(delete_quote.json()["message"]).is_equal_to("Quote deleted successfully")
            assert_that(delete_quote.headers["content-type"]).is_equal_to("application/json")
            assert_that(delete_quote.headers["server"]).is_equal_to("uvicorn")
            assert_that(delete_quote.headers["x-egnyte"]).is_not_empty()
            # assert get non-existing quote
            assert_that(get_quote_with_id.json()["detail"]).is_equal_to(f"Quote with {quote_id} doesn't exist.")
            assert_that(get_quote_with_id.headers["content-type"]).is_equal_to("application/json")
            assert_that(get_quote_with_id.headers["server"]).is_equal_to("uvicorn")
            assert_that(get_quote_with_id.headers["x-egnyte"]).is_not_empty()

    # POST, PUT, GET, DELETE with id - 200
        # POST
        create_quote = requests.post("http://127.0.0.1:8080/quote/",
                                     headers={
                                         "accept": "application/json",
                                         "Content-Type": "application/json"
                                     },
                                     json={
                                         "quote": "I never dreamed about success, I worked for it.",
                                         "author": "Estee Lauder"
                                     })
        # PUT created quote it:
        quote_id = create_quote.json()["data"][0]["id"]
        update_quote_with_id = requests.put(f"http://127.0.0.1:8080/quote/{quote_id}",
                                            headers={
                                                "accept": "application/json",
                                                "Content-Type": "application/json"
                                            },
                                            json={
                                                "quote": "You’ve got to get up every morning with determination if you’re "
                                                         "going to go to bed with satisfaction.",
                                                "author": "George Lorimer."
                                            })
        # GET with id
        get_created_quote_with_id = requests.get(f"http://127.0.0.1:8080/quote/{quote_id}",
                                                 headers={"accept": "application/json"})
        # DELETE
        delete_quote = requests.delete(f"http://127.0.0.1:8080/quote/{quote_id}",
                                       headers={"accept": "application/json"})
        # GET with id
        get_non_existing_quote_with_id = requests.get(f"http://127.0.0.1:8080/quote/{quote_id}",
                                                      headers={"accept": "application/json"})

        with soft_assertions():
            assert_that(create_quote.status_code).is_equal_to(200)
            assert_that(update_quote_with_id.status_code).is_equal_to(200)
            # assert everything
            assert_that(update_quote_with_id.json()["data"][0]).contains("update is successful")
            assert_that(update_quote_with_id.json()["message"]).is_equal_to("Quote updated successfully")
            assert_that(update_quote_with_id.headers["content-type"]).is_equal_to("application/json")
            assert_that(update_quote_with_id.headers["server"]).is_equal_to("uvicorn")
            assert_that(update_quote_with_id.headers["x-egnyte"]).is_not_empty()
            # Verify basic performance sanity
            assert_that(update_quote_with_id.elapsed).is_less_than_or_equal_to(timedelta(milliseconds=500))
            # assert get existing quote
            assert_that(get_created_quote_with_id.json()["message"]).is_equal_to("Quote data retrieved successfully")
            # assert delete
            assert_that(delete_quote.json()["data"][0]).is_equal_to(f"Quote with ID: {quote_id} removed")
            assert_that(delete_quote.json()["message"]).is_equal_to("Quote deleted successfully")
            # assert get non-existing quote
            assert_that(get_non_existing_quote_with_id.json()["detail"]).is_equal_to(
                f"Quote with {quote_id} doesn't exist.")

    # NEGATIVE and VALID data
    # 1. Perform POST with GET method - 403
    # 2. POST quote, DETELE with is - 404

    # NEGATIVE witg INVALID input
    # 1. POST quote with additional payload fields
    # 2. POST quote with empty string
    # 3. POST quote with special characters (chaos fonds)
