import datetime
from io import StringIO

import pandas as pd
import streamlit as st

import plotly.express as px

st.write("### Exploring the leaves")

uploaded_files = st.sidebar.file_uploader(
    "Upload the file from BambooHR", accept_multiple_files=True, type=["xlsx"]
)


@st.cache(allow_output_mutation=True, suppress_st_warning=True)
def load_data(uploaded_files):

    data = []

    progress_bar = st.sidebar.progress(0)

    if len(uploaded_files) > 0:

        for i, uploaded_file in enumerate(uploaded_files):

            uploaded_file.seek(0)
            df_imported = pd.read_excel(uploaded_file)
            data.append(df_imported)
            progress_bar.progress(float((i + 1) / len(uploaded_files)))

        data = pd.concat(data, axis=0, ignore_index=True)
        return data

    else:
        return None


df = load_data(uploaded_files)


if df is not None:
    df['Total hours leave'] = df['Sick days'] 
    start_date = datetime.datetime(2022, 1, 1)
    df['nb_days_ooo'] = df['Total hours leave'] /8
    df['nb_days_total'] = (datetime.datetime.today() - pd.to_datetime(df['Hire date'])).dt.days
    df['percentage_of_ooo_days'] = (df['nb_days_ooo'] / df['nb_days_total']) * 100

    df_per_departement = df.groupby('Departement').mean().reset_index()
    df_per_level = df.groupby('Level').mean().reset_index()
    fig = px.bar(df_per_departement, x='Departement', y='percentage_of_sick_days')
    fig.update_layout(title='Average percentage of sick days per Departement')
    st.plotly_chart(fig, use_container_width=True)

    fig = px.bar(df_per_level, x='Level', y='percentage_of_sick_days')
    fig.update_layout(title='Average percentage of sick days per Level')
    st.plotly_chart(fig, use_container_width=True)

    fig = px.bar(df.sort_values('percentage_of_sick_days', ascending=False).head(10), x='First Name', y='percentage_of_sick_days')
    fig.update_layout(title='Most sick days ranking')

    st.plotly_chart(fig, use_container_width=True)

    fig = px.bar(df.sort_values('percentage_of_sick_days').head(10), x='First Name', y='percentage_of_sick_days')
    fig.update_layout(title='Least sick days ranking')

    st.plotly_chart(fig, use_container_width=True)

else:

    st.info("Upload a file")
