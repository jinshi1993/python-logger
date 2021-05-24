from logger import logger


def test_log():
    log = logger.get_logger()
    log.debug("this is debug log")
    log.warning("this is warning log")
    log.info("this is info log")
    log.error("this is error log")
    log.critical("this is critical log")


def main():
    test_log()


if __name__ == '__main__':
    main()
