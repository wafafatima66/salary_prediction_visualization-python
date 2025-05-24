import streamlit as st
from report import show_report_page
from predict import show_predict_page
from analysis import show_analysis_page

st.header('')
page = st.sidebar.selectbox("Data Prediction & Visualization",("Data Prediction" , "Data Visualization"))


if page == "Data Prediction":
    show_predict_page()
elif page == "Data Visualization":
    page2 = st.sidebar.radio(
     "Select",
     ('Yearly Report', 'Comparison Report'))
    if page2 == "Yearly Report":
        show_report_page()
    elif page2 == "Comparison Report":
        show_analysis_page()
else :
    st.write("""#### No page Selected """ )