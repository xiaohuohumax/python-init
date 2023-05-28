import logging.config

from ruamel import yaml

from app.util import read_file, path_exists, abs_path

# 默认日志配置
default_config = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'simple': {
            'format': '%(asctime)s %(levelname)s: %(message)s'
        },
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'level': 'DEBUG',
            'formatter': 'simple',
            'stream': 'ext://sys.stdout'
        },
    },
    'root': {
        'level': 'DEBUG',
        'handlers': ['console']
    }
}


def init_log(log_config_path: str) -> None:
    """
    配置日志

    :param log_config_path: 日志配置文件路径
    """
    global default_config
    try:
        config_dict = default_config

        if path_exists(log_config_path):
            config_dict = yaml.safe_load(read_file(log_config_path))

        if config_dict is None:
            config_dict = default_config
        logging.config.dictConfig(config_dict)
    except Exception as e:
        logging.config.dictConfig(default_config)
        logging.warning(f'日志配置异常,采用默认配置:{e}')


# 配置日志
init_log(abs_path('./resource/config/log.yaml'))
