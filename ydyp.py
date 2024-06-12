import sys

def main():
    # 从命令行参数中获取参数值
    token = sys.argv[1]

    if token:
        print("成功获取参数:", token)
    else:
        print("未找到参数或参数为空")

if __name__ == "__main__":
    main()
