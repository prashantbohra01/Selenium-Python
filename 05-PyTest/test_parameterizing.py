# Parameterizing test with multiple data sets using fixtures

import pytest

def test_crossBrowser(crossBrowser):
    print(crossBrowser[0])  # the test will run 3 times but only the value at 0th index would be printed