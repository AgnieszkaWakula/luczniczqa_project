import pytest


@pytest.fixture(scope="class")
def one():
    print("\nI will execute THIS before at class start")
    my_list = [1, 2, 3]
    yield my_list[0]
    print("\nI will be executed AFTER all of the tests")


@pytest.fixture(scope="function") #this is default scope of pytest fixture
def two():
    print("\nI will be executed AT START of test method")
    yield
    print("\nI will be executed AT THE END of test method")

def test_123(one, two):
    print(one)
    print("I'm the test method")