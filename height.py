import streamlit as st
import pandas as pd

df = pd.DataFrame(
    [
       {"명령어": "st.selectbox", "평점": 4, "is_widget": True},
       {"명령어": "st.balloons", "평점": 5, "is_widget": False},
       {"명령어": "st.time_input", "평점": 3, "is_widget": True},
   ]
)
edited_df = st.experimental_data_editor(df, height = 300, num_rows="fixed")

favorite_command = edited_df.loc[edited_df["평점"].idxmax()]["명령어"]

edited_df = st.experimental_data_editor(df, height = None, num_rows="fixed")

favorite_command = edited_df.loc[edited_df["평점"].idxmax()]["명령어"]
