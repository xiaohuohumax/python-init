import re

from .app import App
from .args import global_args
from .conf import global_config
from .log import *
from .util import attr_links


def show_banner(banner_path: str) -> None:
    """
    显示 banner

    :param banner_path: banner 文件路径 
    """
    if not path_exists(banner_path):
        return
    banner_data = read_file(banner_path)

    for match_item in set(re.findall(r'(\$config(\.(\w+(\[\d+\])?))+\$)', banner_data)):
        config_link = match_item[0][8:-1]
        try:
            config_attr = attr_links(global_config, config_link)
            banner_data = banner_data.replace(match_item[0], config_attr)
        except Exception as e:
            logging.debug(f'未找到配置:{config_link} {e}')

    [logging.info(line) for line in banner_data.split('\n')]


if global_config.app.is_show_banner:
    show_banner(abs_path('./resource/banner.txt'))
