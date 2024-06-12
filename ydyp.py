import os

# 从环境变量中获取参数
env_name = 'ydypCK'
token = os.getenv(env_name)

if token:
    print("成功获取参数:", token)
else:
    print("未找到环境变量或参数为空")
