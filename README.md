# python-logger
- 一个基于官方logging库的自定义Python日志模块

# 依赖
- Python >= 2.6.6

# 用法
```python
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
```

# 预览
```shell
2021-05-25 01:50:18,798 [DEBUG   ] 10340 :140183332554560 main.py         6    | this is debug log
2021-05-25 01:50:18,798 [WARNING ] 10340 :140183332554560 main.py         7    | this is warning log
2021-05-25 01:50:18,798 [INFO    ] 10340 :140183332554560 main.py         8    | this is info log
2021-05-25 01:50:18,799 [ERROR   ] 10340 :140183332554560 main.py         9    | this is error log
2021-05-25 01:50:18,799 [CRITICAL] 10340 :140183332554560 main.py         10   | this is critical log
```