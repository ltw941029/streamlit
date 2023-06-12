import streamlit as st

uploaded_file = st.file_uploader("파일을 선택해주세요", label_visibility = "hidden")

uploaded_file = st.file_uploader("파일을 선택해주세요", label_visibility = "visible")

uploaded_file = st.file_uploader("파일을 선택해주세요", label_visibility = "collapsed")
