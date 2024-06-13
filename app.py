import streamlit as st
import subprocess

# 定义要运行的 Python 脚本
def run_script(token):
    script = f"""
import time

token = '{token}'

print(f"Token: {token}")

# 模拟一些计算
for i in range(5):
    print(f"运行中... {i+1}")
    time.sleep(1)

print("脚本运行完成")
"""
    return script

# Streamlit 应用
def main():
    st.title("运行嵌入式脚本")
    
    # 用户输入参数
    token = st.text_input("输入 Token")
    
    # 确认按钮
    if st.button("运行脚本"):
        with st.spinner("脚本运行中..."):
            script = run_script(token)
            # 写入临时文件
            with open("temp_script.py", "w") as file:
                file.write(script)
            
            # 运行脚本并捕获输出
            result = subprocess.run(["python", "temp_script.py"], capture_output=True, text=True)
            
            st.success("脚本运行完成")
            st.subheader("日志输出")
            st.text(result.stdout)
            if result.stderr:
                st.error("脚本错误日志")
                st.text(result.stderr)

if __name__ == "__main__":
    main()
