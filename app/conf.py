from dataclasses import dataclass
from dataclasses import field

from dacite import from_dict
from ruamel import yaml

from .util import path_exists, abs_path, read_file


@dataclass
class AppConfig:
    """
    项目配置
    """
    # 版本
    version: str = ''
    # app 名称
    name: str = 'python-init'
    # 是否显示 banner
    is_show_banner: bool = True
    ...


@dataclass
class Config:
    """
    配置对象
    """
    app: AppConfig = field(default_factory=AppConfig)
    # 其他参数可自行扩展
    ...

    def __post_init__(self):
        # 参数设置后自动调用, 详见解释 dataclasses
        ...


def init_config(config_path: str) -> Config:
    """
    加载配置信息映射到实体类 (配置文件不存在则采用默认配置)

    :param config_path: 配置文件路径
    :return: 配置对象
    """
    config_dict = None
    if path_exists(config_path):
        config_dict = yaml.safe_load(read_file(config_path))

    if config_dict is None:
        config_dict = {}

    return from_dict(data_class=Config, data=config_dict)


# 全局配置
global_config = init_config(abs_path('./resource/config/application.yaml'))
