# to execute pytest for selected file you have to give the file name in command "pytest test_Demo2.py -v -s"

# to execute specific test cases from different file use this method "pytest -k {specific keyword} -v -s"

# -k stands for methods name execution
# -v stands for more info metadata
# -s stands for logs in output

# You can mark (tag) tests "@pytest.mark.tagname" and then run with -m 
# Mainly used for smoke and regression testing

# We can Skip the test cases by using "@pytest.mark.skip"
# We can use this where we want the test case but dont want the report of it "@pytest.mark.xfail"


import pytest

@pytest.mark.skip
def testPrograms():
    msg = "Hello"

    assert msg == "Hi", "Test failed because strings did not matched"

@pytest.mark.smoke
def testCreditcardAddition():
    a = 4
    b = 6

    assert a+2 == b, "The addition did not passed" 