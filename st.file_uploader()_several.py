import streamlit as st

uploaded_files = st.file_uploader("CSV 파일을 선택해주세요 ", accept_multiple_files=True)
for uploaded_file in uploaded_files:
    bytes_data = uploaded_file.read()
    st.write("파일 이름:", uploaded_file.name)
    st.write(bytes_data)
