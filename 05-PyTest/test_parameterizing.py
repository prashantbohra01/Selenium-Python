# Parameterizing test with multiple data sets using fixtures

#data driven and parameterization can be done with return statement in tuple format
# when you define fixture scope to class only, it will run once before class is initiated and at the end

import pytest

def test_crossBrowser(crossBrowser):
    print(crossBrowser[0])  # the test will run 3 times but only the value at 0th index would be printed



# HTML reports

# We have to first install html reports by using "pip install pytest-html"
# then we can use the command to make a html report for the tests present in that folder "pytest --html=report.html"
# After using this command we can see a new file which is report.html is generated
# copy the path of report.html file and paste it in your browser to see all the reports of the tests
