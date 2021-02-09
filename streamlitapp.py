import numpy as np
import pandas as pd
import streamlit as st
import base64
from pandas_profiling import ProfileReport
import pandas_profiling
from streamlit_pandas_profiling import st_profile_report

datasets = {"ABS - G44": ["data/g44.csv", "Census 2016, G44 Labour force status by sex of parents by age of dependent children for Couple families (SA2+)"], "ABS - G45": ["data/g45.csv", "Census 2016, G45 Labour force status by sex of parent by age of dependent children for one parent families (SA2+)"]}

# Sidebar
with st.sidebar.header('Select Data'):
    dataset_selector = st.sidebar.selectbox(
    "Select what dataset you would like to explore.",
    ("ABS - G44", "ABS - G45")
)

# Web App Title
st.markdown(f'''
# **Exploratory Data App**
---
- Dataset Selector is in the sidebar :)

Currently Exploring: {datasets[dataset_selector][1]}
''')

# Can produce runtime error if datasize exceeds 50.0MB
# e.g. "RuntimeError: Data of size 54.3MB exceeds write limit of 50.0MB"
@st.cache
def download_link(object_to_download, download_filename, download_link_text):
    """
    Generates a link to download the given object_to_download.

    object_to_download (str, pd.DataFrame):  The object to be downloaded.
    download_filename (str): filename and extension of file. e.g. mydata.csv, some_txt_output.txt
    download_link_text (str): Text to display for download link.

    Examples:
    download_link(YOUR_DF, 'YOUR_DF.csv', 'Click here to download data!')
    download_link(YOUR_STRING, 'YOUR_STRING.txt', 'Click here to download your text!')

    """
    if isinstance(object_to_download,pd.DataFrame):
        object_to_download = object_to_download.to_csv(index=False)

    # some strings <-> bytes conversions necessary here
    b64 = base64.b64encode(object_to_download.encode()).decode()

    return f'<a href="data:file/txt;base64,{b64}" download="{download_filename}">'

# Load CSV
@st.cache
def load_csv(filename):
    df = pd.read_csv(filename, low_memory=False)
    return df

# Pandas Profiling Report
@st.cache
def HTMLContainer_hash_func(HTMLContainer):
    hashed_container = hash(HTMLContainer)
    return hashed_container

@st.cache
def HTMLHTML_hash_func(HTMLHTML):
    hashed_container = hash(HTMLHTML)
    return hashed_container

@st.cache(hash_funcs={pandas_profiling.report.presentation.flavours.html.container.HTMLContainer: HTMLContainer_hash_func, pandas_profiling.report.presentation.flavours.html.html.HTMLHTML: HTMLHTML_hash_func}, allow_output_mutation=True)
def load_profile(df):
    pr = ProfileReport(df, explorative=True)
    return pr


df = load_csv(datasets[dataset_selector][0])
pr = load_profile(df)

st.header('**Input DataFrame**')
st.write(df)

if st.button('Download data'):
    tmp_download_link = download_link(df, "abs_data.csv", 'Click here to download your data!')
    st.markdown(tmp_download_link, unsafe_allow_html=True)

st.write('---')
st.header('**Profiling Report**')
st_profile_report(pr)