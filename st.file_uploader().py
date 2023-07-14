import streamlit as st
import pandas as pd

uploaded_file = st.file_uploader("파일을 선택해주세요")
if uploaded_file is not None:

    # "파일과 유사한" 개체가 허용되는 모든 곳에서 사용 가능:
    dataframe = pd.read_csv(uploaded_file)
    st.write(dataframe)
