import streamlit as st

uploaded_file = st.file_uploader("파일을 선택해주세요", key=1, label_visibility='collapsed')

uploaded_file = st.file_uploader("파일을 선택해주세요", key=2, label_visibility='visibl')

uploaded_file = st.file_uploader("파일을 선택해주세요", key=3, label_visibility='hidden')
