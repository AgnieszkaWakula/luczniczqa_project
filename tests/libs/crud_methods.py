import requests


def request_method(method):
    def decorator(response):
        def wrapper(*args, **kwargs):
            return requests.request(method, *args, **kwargs)

        return wrapper

    return decorator


@request_method("POST")
def create(self, url, headers, auth, json, timeout=7):
    pass


@request_method("GET")
def read(self, url, headers, auth, json, timeout=7):
    pass


@request_method("PUT")
def update(self, url, headers, auth, json, timeout=7):
    pass


@request_method("DELETE")
def delete(self, url, headers, auth, json, timeout=7):
    pass
