# Fixtures are used as setup and tear down methods for test cases
# conftest file is used to generalize fixtures and make it available to all test cases

import pytest

@pytest.fixture(scope="class")
def setup():
    print("i will be executing first")
    yield
    print("I will be executed last")


@pytest.fixture()
def dataLoad():
    print("User profile data is being created")
    return ["Prashant", "Bohra", "abc.com"]