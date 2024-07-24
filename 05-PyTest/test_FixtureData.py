import pytest

@pytest.mark.usefixtures("dataLoad")
class TestExample1:

    def testData(self, dataLoad):
        print(dataLoad)
        print(dataLoad[0])
        print(dataLoad[2])