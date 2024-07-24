# Pytest file name should start with "test_" or end with "_test"

# Pytest methods/function name should always start with "test"

# Any code should be wrapped in methods

# command for pytest to run in cmd is "pytest -v -s" or "py.test -v -s"
import pytest


@pytest.mark.smoke
def testFirstProgram():
    print("Hello-World")


def testCreditcardGreetAll():
    print("Good Morning")
