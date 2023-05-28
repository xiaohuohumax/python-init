import argparse

from .conf import global_config

parser = argparse.ArgumentParser(description=global_config.app.name)
parser.add_argument('-c,--console', dest='console', type=str, help='console message',
                    default=f'hello {global_config.app.name}')
# 其他配置自行扩展
# parser.add_argument(...)
...
# 全局命令行参数
global_args = parser.parse_args()
