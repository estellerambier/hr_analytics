from pathlib import Path

import streamlit as st

st.markdown("How are these numbers computed?")
st.sidebar.markdown("# 👩‍🔬 Methodo")
tab1, tab2 = st.tabs(["Tracking OOO days", "Inclusivity"])


btn = st.button("Celebrate!")
if btn:
    st.balloons()
