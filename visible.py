import streamlit as st

uploaded_file = st.file_uploader("파일을 선택해주세요", type = ['png', 'jpg'], label_visibility = "hidden")
for uploaded_file in uploaded_files:
    bytes_data = uploaded_file.read()
    st.write("파일 이름:", uploaded_file.name)
    st.write(bytes_data)
