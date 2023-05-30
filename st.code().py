import streamlit as st

code = '''def 안녕():
    print("안녕, Streamlit!")'''
st.code(code, language='python')
