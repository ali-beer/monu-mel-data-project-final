import numpy as np
import pandas as pd
import streamlit as st
import base64
from pandas_profiling import ProfileReport
import pandas_profiling
from streamlit_pandas_profiling import st_profile_report

datasets = {
    "AEDC - Social": [
        "data/AEDC/social.csv",
        """
        The Australian Early Development Census (AEDC) is a population-based measure of how children in Australia have developed by the time they start their first year of full-time school. Teachers complete a research tool, the Australian version of the Early Development Instrument (the Instrument) for each child in their class. The Instrument measures five key areas, or domains, of early childhood development:
        - physical health and wellbeing
        - social competence
        - emotional maturity
        - language and cognitive skills (school-based)
        - communication skills and general knowledge.
        These areas are closely linked to the predictors of adult health, education and social outcomes. The Council of Australian Governments (COAG) has endorsed the AEDC as a national progress measure of early childhood development in Australia.
        """
        ],
    "AEDC - Emotional": [
        "data/AEDC/emotional.csv", 
        """
        The Australian Early Development Census (AEDC) is a population-based measure of how children in Australia have developed by the time they start their first year of full-time school. Teachers complete a research tool, the Australian version of the Early Development Instrument (the Instrument) for each child in their class. The Instrument measures five key areas, or domains, of early childhood development:
        - physical health and wellbeing
        - social competence
        - emotional maturity
        - language and cognitive skills (school-based)
        - communication skills and general knowledge.
        These areas are closely linked to the predictors of adult health, education and social outcomes. The Council of Australian Governments (COAG) has endorsed the AEDC as a national progress measure of early childhood development in Australia.
        """
        ],
    "AEDC - Communication": ["data/AEDC/communication.csv", """
        The Australian Early Development Census (AEDC) is a population-based measure of how children in Australia have developed by the time they start their first year of full-time school. Teachers complete a research tool, the Australian version of the Early Development Instrument (the Instrument) for each child in their class. The Instrument measures five key areas, or domains, of early childhood development:
        - physical health and wellbeing
        - social competence
        - emotional maturity
        - language and cognitive skills (school-based)
        - communication skills and general knowledge.
        These areas are closely linked to the predictors of adult health, education and social outcomes. The Council of Australian Governments (COAG) has endorsed the AEDC as a national progress measure of early childhood development in Australia.
        """],
    "AEDC - Health": ["data/AEDC/health.csv", """"
        The Australian Early Development Census (AEDC) is a population-based measure of how children in Australia have developed by the time they start their first year of full-time school. Teachers complete a research tool, the Australian version of the Early Development Instrument (the Instrument) for each child in their class. The Instrument measures five key areas, or domains, of early childhood development:
        - physical health and wellbeing
        - social competence
        - emotional maturity
        - language and cognitive skills (school-based)
        - communication skills and general knowledge.
        These areas are closely linked to the predictors of adult health, education and social outcomes. The Council of Australian Governments (COAG) has endorsed the AEDC as a national progress measure of early childhood development in Australia.
        """],
    "AEDC - Language": ["data/AEDC/language.csv", """
        The Australian Early Development Census (AEDC) is a population-based measure of how children in Australia have developed by the time they start their first year of full-time school. Teachers complete a research tool, the Australian version of the Early Development Instrument (the Instrument) for each child in their class. The Instrument measures five key areas, or domains, of early childhood development:
        - physical health and wellbeing
        - social competence
        - emotional maturity
        - language and cognitive skills (school-based)
        - communication skills and general knowledge.
        These areas are closely linked to the predictors of adult health, education and social outcomes. The Council of Australian Governments (COAG) has endorsed the AEDC as a national progress measure of early childhood development in Australia.
        """],
    "AEDC - One or more": ["data/AEDC/oneormore.csv", """
        The Australian Early Development Census (AEDC) is a population-based measure of how children in Australia have developed by the time they start their first year of full-time school. Teachers complete a research tool, the Australian version of the Early Development Instrument (the Instrument) for each child in their class. The Instrument measures five key areas, or domains, of early childhood development:
        - physical health and wellbeing
        - social competence
        - emotional maturity
        - language and cognitive skills (school-based)
        - communication skills and general knowledge.
        These areas are closely linked to the predictors of adult health, education and social outcomes. The Council of Australian Governments (COAG) has endorsed the AEDC as a national progress measure of early childhood development in Australia.
        """],
    "AEDC - Two or more": ["data/AEDC/twoormore.csv", """
        The Australian Early Development Census (AEDC) is a population-based measure of how children in Australia have developed by the time they start their first year of full-time school. Teachers complete a research tool, the Australian version of the Early Development Instrument (the Instrument) for each child in their class. The Instrument measures five key areas, or domains, of early childhood development:
        - physical health and wellbeing
        - social competence
        - emotional maturity
        - language and cognitive skills (school-based)
        - communication skills and general knowledge.
        These areas are closely linked to the predictors of adult health, education and social outcomes. The Council of Australian Governments (COAG) has endorsed the AEDC as a national progress measure of early childhood development in Australia.
        """]
    }

# Sidebar
with st.sidebar.header('Select Data'):
    dataset_selector = st.sidebar.selectbox(
    "Select what dataset you would like to explore.",
    list(datasets.keys())
)

# Web App Title
st.markdown(f'''
# **Exploratory Data App**
---
- This app provides a simple, first glance overview of our datasets, prior to our analysis.
- Dataset Selector is in the sidebar :)

**Currently Exploring:** {dataset_selector}

**Description:** {datasets[dataset_selector][1]}

**Useful Resources:**
- [2018 AEDC Data Collection Technical Report](https://www.aedc.gov.au/Websilk/Handlers/ResourceDocument.ashx?id=54a02864-db9a-6d2b-9fad-ff0000a141dd)
- [Report on the quality of 2016 Census data](https://www.abs.gov.au/websitedbs/d3310114.nsf/home/Independent+Assurance+Panel/$File/CIAP+Report+on+the+quality+of+2016+Census+data.pdf)
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

st.write('---')
st.header('**Profiling Report**')
st_profile_report(pr)