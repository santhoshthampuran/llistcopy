import logging


def getLogger(name):
    # create logger
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)

    # create console handler
    chdlr = logging.StreamHandler()
    # chdlr.setLevel(logging.DEBUG)

    # create file handler
    fhdlr = logging.FileHandler(filename="log.txt", mode="a")
    # since it is file, I'll need more details like the time
    fhdlr.setFormatter(logging.Formatter("%(asctime)s - %(filename)s - %(levelname)s - %(message)s"))
    formatter = logging.Formatter("%(levelname)s:%(message)s")
    chdlr.setFormatter(formatter)
    logger.addHandler(chdlr)
    logger.addHandler(fhdlr)

    return logger
