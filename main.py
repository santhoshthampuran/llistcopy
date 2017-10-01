import logging

logger = logging.getLogger("main.py")
logging.basicConfig()


# fh = logging.FileHandler("log.txt")
# formatter = logging.Formatter("%(asctime)s - %(name)s - %(level)s - \
#    %(message)s")
# fh.setFormatter(formatter)
# logger.addHandler(fh)


logger.setLevel(logging.DEBUG)

logger.info("this is a test message %s %s", "yes", "no")
