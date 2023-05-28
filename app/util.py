from pathlib import Path
from typing import Any


def abs_path(rel_path: str) -> str:
    """
    相对路径转绝对路径(相对于项目根目录)

    :param rel_path: 相对路径
    :return: 绝对路径
    """
    return str(Path(Path(__file__).parent.parent, rel_path))


def path_exists(file_path: str) -> bool:
    """
    判断路径是否存在

    :param file_path: 文件路径
    :return: 是否存在
    """
    return Path(file_path).exists()


def read_file(file_path: str, encoding: str = 'utf8') -> str:
    """
    读取文件内容

    :param file_path: 文件路径
    :param encoding: 编码格式默认utf8
    :return: 文件内容
    """
    with open(file_path, encoding=encoding) as f:
        return f.read()


def write_file(file_path: str, data: str, encoding: str = 'utf8', mode='w') -> None:
    """
    写入文件

    :param file_path: 文件路径
    :param data: 写入数据
    :param encoding: 编码格式
    :param mode: 写入模式默认w
    """
    with open(file_path, encoding=encoding, mode=mode) as f:
        f.write(data)


def attr_links(obj: Any, links: str) -> Any:
    """
    通过属性链获取对象属性

    obj:
        {hobby: [{ id: 1, name: 'code' }]}
    links:
        'hobby[0].name' => code

    :param obj: 对象
    :param links: 属性链
    :return: 对象属性值
    """
    for attr in links.split('.'):
        if '[' in attr:
            arr_index = int(attr[attr.index('[') + 1:attr.index(']')])
            obj = obj[arr_index]
            attr = attr[:attr.index('[')]
        obj = getattr(obj, attr)
    return obj
