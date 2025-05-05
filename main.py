import streamlit as st

st.write("تم فتح التطبيق")

# مسار الملف
file_path = 'output/html_files/html_1.html'

try:
    # محاولة فتح الملف وقراءة محتواه
    with open(file_path, 'r', encoding='utf-8') as file:
        html_code = file.read()
        st.markdown(html_code, unsafe_allow_html=True)
except FileNotFoundError:
    # إذا كان الملف غير موجود
    st.error(f"الملف مش موجود: {file_path}")
except Exception as e:
    # في حالة وجود أي خطأ آخر
    st.error(f"حصل خطأ: {e}")
