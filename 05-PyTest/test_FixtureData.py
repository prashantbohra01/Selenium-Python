import pytest
from BaseClass import BaseClass

@pytest.mark.usefixtures("dataLoad")
class TestExample1(BaseClass):

    def test_editData(self, dataLoad):
        log = self.getLogger()
        log.info(dataLoad[0])
        log.info(dataLoad[2])
