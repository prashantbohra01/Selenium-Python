import logging


def test_loggingDemo():
    logger = logging.getLogger(__name__)
    fileHandler = logging.FileHandler('05-PyTest\logFile.log')
    formatter = logging.Formatter("%(asctime)s :%(levelname)s : %(name)s : %(message)s")
    fileHandler.setFormatter(formatter)

    logger.addHandler(fileHandler)  # fileHandler object 

    logger.setLevel(logging.DEBUG)

    logger.debug("A debug statement is executed")  # same as print statement

    logger.info("Information regarding the test case")

    logger.warning("Test case pass with a warning message")

    logger.error("Test case fail")

    logger.critical("Important test case failed on which other test case depend")
