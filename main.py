import streamlit as st

st.write("تم فتح التطبيق")

try:
    with open('output/html_files/html_1.html', 'r', encoding='utf-8') as file:
        html_code = file.read()
        st.markdown(html_code, unsafe_allow_html=True)
except FileNotFoundError:
    st.error("الملف مش موجود: output/html_files/html_1.html")
except Exception as e:
    st.error(f"حصل خطأ: {e}")
