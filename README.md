# Python-Init

🔥Python简单初始项目(空项目只有基础辅助功能)🔥

## 🔨 基础辅助功能

+ 全局配置(映射配置文件全局使用, yaml格式)

```python
# [使用]
# 修改配置 yaml (resource/config/application.yaml)
# 导入 global_config 即可
from app.conf import global_config

print(global_config.app)
...

# [扩展配置]
# 在 app.conf.Config 添加配置对象以及默认属性值(配置可嵌套)
# 然后在配置文件 application.yaml 添加对应配置, 即可自动映射
```

+ 全局参数(拦截命令行参数全局使用)

```python
# [使用]
# python main.py -c "hello world"
from app.args import global_args

print(global_args.console)
# [查看帮助]
# python main.py -h
# [自定义参数]
# 修改/添加 app.args.parser 即可
```

+ 日志(设置全局日志输出格式) 

```yaml
# 修改 resource/config/log.yaml
```
+ banner(可使用全局配置)

```text
# 前缀固定 config.* 且开头结尾用$包围
$config.app.version$
```

## 📦 安装/管理依赖 pipenv

```shell
# 安装 pipenv
pip install pipenv -i ...
# 安装依赖 [注意若安装依赖慢,请更换 Pipfile 文件中仓库地址]
# [[source]]
# url = "..."
pipenv install
# 添加其他依赖
pipenv install some-packages
```

## 🏃 运行

```shell
python main.py [command]
# [帮助]
python main.py -h
```

## 🐋 Docker

```shell
# [构建]
docker build -t python-init:latest .
# [运行]
docker run -d python-init:latest python main.py
```

## 🌳 结构

```text
python-init
 ├── app
 │   ├── app.py
 │   ├── args.py
 │   ├── conf.py
 │   ├── log.py
 │   ├── util.py
 │   └── __init__.py
 ├── Dockerfile
 ├── init_env.sh
 ├── LICENSE
 ├── log
 │   └── app.log
 ├── main.py
 ├── Pipfile
 ├── Pipfile.lock
 ├── README.md
 └── resource
     ├── banner.txt
     └── config
         ├── application.yaml
         └── log.yaml
```