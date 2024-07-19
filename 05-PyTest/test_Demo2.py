# to execute pytest for selected file you have to give the file name in command "pytest test_Demo2.py -v -s"

# to execute specific test cases from different file use this method "pytest -k {specific keyword} -v -s"

# -k stands for methods name execution
# -v stands for more info metadata
# -s stands for logs in output


def testPrograms():
    msg = "Hello"

    assert msg == "Hi", "Test failed because strings did not matched"

def testCreditcardAddition():
    a = 4
    b = 6

    assert a+2 == b, "The addition did not passed" 