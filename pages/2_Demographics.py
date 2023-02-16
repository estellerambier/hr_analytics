import datetime
from io import StringIO

import pandas as pd
import streamlit as st

import plotly.express as px

st.write("### Exploring your employees")

# Button on the side
uploaded_files = st.sidebar.file_uploader(
    "Upload the file from BambooHR", accept_multiple_files=True, type=["xlsx"]
)

# DON't change this:
@st.cache(allow_output_mutation=True, suppress_st_warning=True)
def load_data(uploaded_files):

    data = []

    progress_bar = st.sidebar.progress(0)

    if len(uploaded_files) > 0:

        for i, uploaded_file in enumerate(uploaded_files):

            uploaded_file.seek(0)
            df_imported = pd.read_csv(uploaded_file)
            data.append(df_imported)
            progress_bar.progress(float((i + 1) / len(uploaded_files)))

        data = pd.concat(data, axis=0, ignore_index=True)
        return data

    else:
        return None


df = load_data(uploaded_files)

# From here is the ploting
if df is not None:
    # pie chart here:
    df_nationalities = df.groupby('Nationality', as_index=False).count().sort_values(by='Last name, First name')
    fig = px.pie(df_nationalities, values='Last name, First name', names='Nationality', title='Count of employees per Nationalities')
    fig.update_traces(textinfo='value')
    fig.show()

else:

    st.info("Upload a file")
