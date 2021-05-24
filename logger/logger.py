# -*- coding: UTF-8 -*-
import logging.config
from logging.handlers import TimedRotatingFileHandler

# 日志保存路径
LOGGING_FILENAME = 'test.log'

# 日志输出级别
# CRITICAL = 50
# FATAL = CRITICAL
# ERROR = 40
# WARNING = 30
# WARN = WARNING
# INFO = 20
# DEBUG = 10
# NOTSET = 0
LOGGING_LEVEL = 'DEBUG'

# 日志输出格式
LOGGING_FORMAT = '%(asctime)s [%(levelname)-8s] %(process)-6d:%(thread)-8d %(filename)-15s %(lineno)-4d | %(message)s'

# 日志编码
LOGGING_ENCODE = 'utf-8'

# 日志滚动切割时机
LOGGING_ROTATE_PERIOD = 'MIDNIGHT'

# 日志滚动备份数
LOGGING_ROTATE_BACKUPS = 3

fileTimeHandler = TimedRotatingFileHandler(
    filename=LOGGING_FILENAME,
    when=LOGGING_ROTATE_PERIOD,
    backupCount=LOGGING_ROTATE_BACKUPS,
    encoding=LOGGING_ENCODE
)
fileTimeHandler.setFormatter(logging.Formatter(LOGGING_FORMAT))
logging.basicConfig(level=LOGGING_LEVEL)


def get_logger():
    logger = logging.getLogger(__name__)
    logger.propagate = False
    logger.addHandler(fileTimeHandler)
    return logger
