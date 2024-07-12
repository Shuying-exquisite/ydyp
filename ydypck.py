import streamlit as st
import streamlit.components.v1 as components

st.title("获取内嵌网页的 CK")

# 嵌入的网页 URL
embedded_url = "https://yun.139.com/m/#/login"

# 定义 iframe
iframe_code = f"""
<iframe id="embeddedPage" src="{embedded_url}" width="800" height="600"></iframe>
<button onclick="getCK()">获取 CK</button>
<p id="ckValue"></p>

<script>
function getCK() {{
    var iframe = document.getElementById('embeddedPage');
    var iframeWindow = iframe.contentWindow || iframe.contentDocument;
    if (iframeWindow.document) {{
        try {{
            var ckValue = iframeWindow.document.cookie;
            document.getElementById('ckValue').innerText = 'CK: ' + ckValue;
        }} catch (e) {{
            document.getElementById('ckValue').innerText = '无法获取 CK，可能是跨域限制。';
        }}
    }}
}}
</script>
"""

# 渲染 iframe 和按钮
components.html(iframe_code, height=650)
