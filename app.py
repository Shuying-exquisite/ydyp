import streamlit as st
import subprocess
import os

# Streamlit 应用
def main():
    st.title("运行嵌入式脚本")

    # 用户输入环境变量名
    env_name = st.text_input("输入环境变量名")

    # 确认按钮
    if st.button("运行脚本"):
        with st.spinner("脚本运行中..."):
            # 设置环境变量
            os.environ['ydypCK'] = env_name
            # 运行脚本并捕获输出
            result = subprocess.run(["python", "ydyp.py"], capture_output=True, text=True)

            st.success("脚本运行完成")
            st.subheader("日志输出")
            st.text(result.stdout)
            if result.stderr:
                st.error("脚本错误日志")
                st.text(result.stderr)

if __name__ == "__main__":
    main()
