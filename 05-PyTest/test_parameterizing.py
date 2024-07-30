# Parameterizing test with multiple data sets using fixtures

#data driven and parameterization can be done with return statement in tuple format
# when you define fixture scope to class only, it will run once before class is initiated and at the end

import pytest

def test_crossBrowser(crossBrowser):
    print(crossBrowser[0])  # the test will run 3 times but only the value at 0th index would be printed
