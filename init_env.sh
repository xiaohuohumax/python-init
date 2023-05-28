# 日志文件存夹
if [ ! -d log ]; then mkdir log; fi
# 更新pip
python -m pip install --upgrade pip -i https://pypi.tuna.tsinghua.edu.cn/simple
# 安装pipenv
pip install pipenv -i https://pypi.tuna.tsinghua.edu.cn/simple
# 安装项目依赖
pipenv install --system --deploy
