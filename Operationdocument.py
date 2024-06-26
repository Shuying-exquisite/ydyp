import streamlit as st
from markdown import markdown
from bs4 import BeautifulSoup

# 读取 Markdown 文件
with open("Operationdocument.md", "r", encoding="utf-8") as file:
    markdown_text = file.read()

# 使用 BeautifulSoup 解析 Markdown 文件中的图片引用
html = markdown(markdown_text)
soup = BeautifulSoup(html, 'html.parser')

# 显示 Markdown 文件中的文字内容
st.markdown(markdown_text, unsafe_allow_html=True)

# 显示 Markdown 文件中的图片
for img in soup.find_all('img'):
    img_url = img['src']
    st.image(img_url)
