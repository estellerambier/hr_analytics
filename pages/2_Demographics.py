import pandas as pd
import plotly.express as px
import streamlit as st

st.write("### Exploring your employees")

# Button on the side
uploaded_files = st.sidebar.file_uploader(
    "Upload the file from BambooHR", accept_multiple_files=True, type=["csv"]
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
    df_nationalities = (
        df.groupby("Nationality", as_index=False)
        .count()
        .sort_values(by="Last name, First name")
    )
    df_nationalities.columns = ["Nationality", "Number of employees"]

    fig = px.pie(
        df_nationalities,
        values="Number of employees",
        names="Nationality",
        title="Count of employees per Nationalities",
    )
    fig.update_traces(textinfo="value")
    st.plotly_chart(fig, use_container_width=True)

    mapping = pd.read_csv("static/nationalities_to_country.csv")
    mapping.columns = ["Nationality", "country"]
    mapping.loc[len(mapping.index)] = ["United States of America", "USA"]
    mapping.loc[len(mapping.index)] = ["Hellenic (Greece)", "Greece"]
    mapping.loc[len(mapping.index)] = ["Belarussian", "Belarus"]
    mapping.loc[len(mapping.index)] = ["Ukranian", "Ukraine"]

    df_iso = pd.read_csv("static/map_iso.txt", sep="\t")
    df_iso.columns = ["country", "2let", "3let"]
    df_country = mapping.merge(df_nationalities, on="Nationality", how="right").merge(
        df_iso, on="country"
    )
    fig = px.choropleth(
        df_country,
        locations="3let",
        color="Number of employees",
        hover_data=["Number of employees"],
        title="Source employees nationalities",
        color_continuous_scale=px.colors.sequential.Viridis,
    )
    st.plotly_chart(fig, use_container_width=True)
else:

    st.info("Upload a file")
