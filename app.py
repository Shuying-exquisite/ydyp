
import requests
import streamlit as st
import subprocess
import os

# 定义运行脚本的函数
def run_script(token):
    # 运行脚本并捕获输出
    result = subprocess.run(["python", "ydyp.py", token], capture_output=True, text=True)

    # 返回结果
    return result.stdout, result.stderr

# 主函数
def main():
    st.title("ydyp.py 脚本参数设置")

    # 用户输入环境变量值
    token = st.text_input("输入参数")

    # 确认按钮
    if st.button("运行脚本"):
        # 检查参数是否为空
        if token:
            # 运行脚本
            stdout, stderr = run_script(token)

            # 显示输出
            st.subheader("脚本输出")
            st.text(stdout)
            if stderr:
                st.subheader("脚本错误")
                st.text(stderr)
        else:
            st.error("参数不能为空！")

if __name__ == "__main__":
    main()
