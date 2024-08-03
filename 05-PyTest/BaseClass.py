import logging
import inspect

class BaseClass:
    def getLogger(self):
      loggerName = inspect.stack()[1][3]
      logger = logging.getLogger(loggerName)
      fileHandler = logging.FileHandler('logFile.log')
      formatter = logging.Formatter("%(asctime)s :%(levelname)s : %(name)s : %(message)s")
      fileHandler.setFormatter(formatter)

      logger.addHandler(fileHandler)  # fileHandler object 

      logger.setLevel(logging.DEBUG)
      return logger
 