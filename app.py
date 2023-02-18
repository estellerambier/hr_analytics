from pathlib import Path

import streamlit as st

st.set_page_config(
    page_title="People x Data",
    page_icon="👋",
    layout="wide",
    initial_sidebar_state="expanded",
)

if __name__ == "__main__":

    # st.image("quotaclimat/utils/coverquotaclimat.png")

    st.title("Data driven HR information")
    st.markdown(
        "Data tools will not replace HR, but HR who don't use data tools will be replaced by those who do."
    )

    # st.header("Available")
    # st.markdown("Feature request")
