import streamlit as st
import pandas as pd
from io import StringIO

uploaded_file = st.file_uploader("파일을 선택해주세요")
if uploaded_file is not None:
    # 파일을 바이트로 읽는 방법:
    bytes_data = uploaded_file.getvalue()
    st.write(bytes_data)

    # 문자열 기반 IO파일로 변환하는 방법:
    stringio = StringIO(uploaded_file.getvalue().decode("utf-8"))
    st.write(stringio)

    # 파일을 문자열로 읽는 방법:
    string_data = stringio.read()
    st.write(string_data)

    # "파일과 유사한" 개체가 허용되는 모든 곳에서 사용 가능:
    dataframe = pd.read_csv(uploaded_file)
    st.write(dataframe)
