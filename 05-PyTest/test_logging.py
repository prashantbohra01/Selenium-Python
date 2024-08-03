import logging


def test_loggingDemo():
    logger = logging.getLogger(__name__)
    fileHandler = logging.FileHandler('logFile.log')
    formatter = logging.Formatter("%(asctime)s :%(levelname)s : %(name)s : %(message)s")
    fileHandler.setFormatter(formatter)

    logger.addHandler(fileHandler)  # fileHandler object 

    logger.setLevel(logging.DEBUG)

    logger.debug("A debug statement is executed")  # same as print statement

    logger.info("Information statement")

    logger.warning("Something is in warning mode")

    logger.error("A Major error has happend")

    logger.critical("Critical issue")
