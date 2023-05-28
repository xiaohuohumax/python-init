import logging
import time

from .args import global_args
from .conf import global_config


class App:
    def __init__(self):
        self.flag = True
        logging.debug(f'命令参数: {global_args}')
        logging.debug(f'全局配置: {global_config}')
        logging.info('app 运行成功!')

    def print_time(self) -> None:
        """
        打印时间
        """
        while self.flag:
            logging.info(time.strftime("%Y-%m-%d %H:%M:%S"))
            time.sleep(1)

    def close(self) -> None:
        """
        停止
        """
        self.flag = False
