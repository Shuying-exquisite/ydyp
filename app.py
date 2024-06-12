import streamlit as st
import subprocess
import os

def run_script():
    # 运行脚本并捕获输出
    result = subprocess.run(["python", "ydyp.py"], capture_output=True, text=True)

    # 返回结果
    return result.stdout, result.stderr

def main():
    st.title("运行 ydyp.py 脚本")

    # 用户输入环境变量值
    env_value = st.text_input("输入环境变量值")

    # 确认按钮
    if st.button("运行脚本"):
        # 设置环境变量
        os.environ['ydypCK'] = env_value

        # 运行脚本
        stdout, stderr = run_script()

        # 显示输出
        st.subheader("标准输出")
        st.text(stdout)
        
        if stderr:
            st.subheader("标准错误")
            st.text(stderr)

if __name__ == "__main__":
    main()
