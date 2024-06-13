import sys
import os
import subprocess
import streamlit as st

def check_and_upgrade_python():
    # Check current Python version
    major, minor, micro = sys.version_info[:3]
    if (major, minor, micro) != (3, 11, 9):
        st.warning(f"当前 Python 版本是 {major}.{minor}.{micro}，将自动升级到 3.11.9。")
        # Download and install Python 3.11.9
        if sys.platform == "linux" or sys.platform == "darwin":
            # Linux or macOS
            subprocess.check_call(["sudo", "apt-get", "update"])
            subprocess.check_call(["sudo", "apt-get", "install", "-y", "python3.11"])
            subprocess.check_call(["sudo", "apt-get", "install", "-y", "python3.11-venv"])
            subprocess.check_call(["sudo", "apt-get", "install", "-y", "python3.11-pip"])
        elif sys.platform == "win32":
            # Windows
            subprocess.check_call(["powershell", "-Command", "Invoke-WebRequest -Uri https://www.python.org/ftp/python/3.11.9/python-3.11.9-amd64.exe -OutFile python-3.11.9-amd64.exe"])
            subprocess.check_call(["python-3.11.9-amd64.exe", "/quiet", "InstallAllUsers=1", "PrependPath=1"])
        else:
            st.error("不支持的操作系统")
            return False

        # Restart script with new Python version
        os.execl(sys.executable, sys.executable, *sys.argv)
    return True

def install_package(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

required_packages = ["streamlit", "requests", "PyExecJS"]

for package in required_packages:
    try:
        __import__(package.split("==")[0])
    except ImportError:
        st.warning(f"正在安装 {package}...")
        install_package(package)

import requests
import execjs

def run_script(token):
    result = subprocess.run([sys.executable, "ydyp.py", token], capture_output=True, text=True)
    return result.stdout, result.stderr

def main():
    if not check_and_upgrade_python():
        return

    st.title("ydyp.py 脚本参数设置")

    token = st.text_input("输入参数")

    if st.button("运行脚本"):
        if token:
            stdout, stderr = run_script(token)

            st.subheader("脚本输出")
            st.text(stdout)
            if stderr:
                st.subheader("脚本错误")
                st.text(stderr)
        else:
            st.error("参数不能为空！")

if __name__ == "__main__":
    main()
