import streamlit as st
import re

# 读取 Markdown 文件
with open("Operationdocument.md", "r", encoding="utf-8") as file:
    markdown_text = file.read()

# 在 Streamlit 应用中显示 Markdown 内容，同时处理图片
def render_markdown_with_images(markdown_text):
    # 匹配 Markdown 图片语法 ![alt text](image_url)
    pattern = re.compile(r'!\[.*?\]\((.*?)\)')

    # 记录上一个位置
    last_pos = 0

    # 查找所有匹配项
    for match in pattern.finditer(markdown_text):
        # 显示上一个位置到匹配位置之间的文本
        st.markdown(markdown_text[last_pos:match.start()], unsafe_allow_html=True)

        # 显示图片
        img_url = match.group(1)
        st.image(img_url)

        # 更新上一个位置
        last_pos = match.end()

    # 显示剩余的文本
    st.markdown(markdown_text[last_pos:], unsafe_allow_html=True)

# 调用函数显示内容
render_markdown_with_images(markdown_text)
