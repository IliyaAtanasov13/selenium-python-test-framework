import inspect
import logging


def customLogger(logLevel=logging.DEBUG, console_level = None):
    loggerName = inspect.stack()[1][3]
    logger = logging.getLogger(loggerName)
    logger.setLevel(logging.DEBUG) # By default, logs all messages

    # if console_level != None:
    #     ch = logging.StreamHandler() # StreamHandler logs to console
    #     ch.setLevel(console_level)
    #     ch_format = logging.Formatter('%(asctime)s - %(message)s')
    #     ch.setFormatter(ch_format)
    #     logger.addHandler(ch)

    fileHandler = logging.FileHandler('automation.log'.format(loggerName), mode='a') # a for append, w for...
    fileHandler.setLevel((logLevel))

    formatter = logging.Formatter('%(asctime)s - %(name)s - %(message)s', datefmt='%d/%m/%Y %I:%M:%S')
    fileHandler.setFormatter(formatter)
    logger.addHandler(fileHandler)

    return logger