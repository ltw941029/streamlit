import streamlit as st

uploaded_files = st.file_uploader("파일을 선택해주세요", accept_multiple_files=True,type=["png","jpg","jpeg"])
for uploaded_file in uploaded_files:
    bytes_data = uploaded_file.read()
    st.write(bytes_data)
