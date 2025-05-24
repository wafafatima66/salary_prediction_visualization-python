import streamlit as st
import pandas as pd 
import matplotlib.pyplot as plt
from my_function import clean_country_name, clean_types
from my_function import shorten_categories
from my_function import clean_education
from my_function import clean_organization
from my_function import clean_types_18
from my_function import clean_types
from my_function import clean_types_comparison

@st.cache_data
def load_data_era():

    # BEFORE CORONA

    #2018
    df_18 = pd.read_csv("./data/2018.csv")
    df_18 = df_18[["Country","Employment", "ConvertedSalary", "FormalEducation","CompanySize","DevType"]]
    df_18 = df_18.rename({"ConvertedSalary": "Before"}, axis=1)
    
    # education
    df_18 = df_18[df_18["FormalEducation"].notnull()]
    df_18['FormalEducation'] = df_18['FormalEducation'].apply(clean_education)
    df_18 = df_18.rename({"FormalEducation": "Education"}, axis=1)
    
    # company size
    df_18 = df_18[df_18["CompanySize"].notnull()]
    df_18['CompanySize'] = df_18['CompanySize'].apply(clean_organization)
    df_18 = df_18.rename({"CompanySize": "Organization"}, axis=1)
    
     #  dev type
    country_map = shorten_categories(df_18.DevType.value_counts(), 1)
    df_18["DevType"] = df_18["DevType"].map(country_map)
    df_18 = df_18[df_18["DevType"].notnull()]
    df_18['DevType'] = df_18['DevType'].apply(clean_types_comparison)
    df_18 = df_18[df_18["DevType"] != "Other"]

    #2019
    df_19 = pd.read_csv("./data/2019.csv")
    df_19 = df_19[["Country","Employment", "ConvertedComp","EdLevel","OrgSize","DevType"]]
    df_19 = df_19.rename({"ConvertedComp": "Before"}, axis=1)
    
    # education
    df_19 = df_19[df_19["EdLevel"].notnull()]
    df_19['EdLevel'] = df_19['EdLevel'].apply(clean_education)
    df_19 = df_19.rename({"EdLevel": "Education"}, axis=1)

    # company size
    df_19 = df_19[df_19["OrgSize"].notnull()]
    df_19['OrgSize'] = df_19['OrgSize'].apply(clean_organization)
    df_19 = df_19.rename({"OrgSize": "Organization"}, axis=1)
    
    # devtype
    country_map = shorten_categories(df_19.DevType.value_counts(), 1)
    df_19["DevType"] = df_19["DevType"].map(country_map)
    df_19 = df_19[df_19["DevType"].notnull()]
    df_19['DevType'] = df_19['DevType'].apply(clean_types)
    df_19 = df_19[df_19["DevType"] != "Other"]
    
    #CONCAT BEFORE CORONA ERA

    df_list_bf = [df_18,df_19]
    df_bf = pd.concat(df_list_bf)
    df_bf = df_bf[df_bf["Before"].notnull()]
    df_bf = df_bf[df_bf["Before"] <= 250000]
    df_bf = df_bf[df_bf["Before"] >= 10000]
    df_bf = df_bf[df_bf["Employment"] == "Employed full-time"]
    df_bf = df_bf.drop("Employment", axis=1)

    #AFTER CORONA ERA 
    #2020
    df_20 = pd.read_csv("./data/2020.csv")
    df_20 = df_20[["Country","Employment", "ConvertedComp","EdLevel","OrgSize","DevType"]]
    df_20 = df_20.rename({"ConvertedComp": "After"}, axis=1)
    
    # education
    df_20 = df_20[df_20["EdLevel"].notnull()]
    df_20['EdLevel'] = df_20['EdLevel'].apply(clean_education)
    df_20 = df_20.rename({"EdLevel": "Education"}, axis=1)
    
    # company size
    df_20 = df_20[df_20["OrgSize"].notnull()]
    df_20['OrgSize'] = df_20['OrgSize'].apply(clean_organization)
    df_20 = df_20.rename({"OrgSize": "Organization"}, axis=1)

    # devtype
    country_map = shorten_categories(df_20.DevType.value_counts(), 1)
    df_20["DevType"] = df_20["DevType"].map(country_map)
    df_20 = df_20[df_20["DevType"].notnull()]
    df_20['DevType'] = df_20['DevType'].apply(clean_types)
    df_20 = df_20[df_20["DevType"] != "Other"]
        
    # 2021
    df_21 = pd.read_csv("./data/2021.csv")
    df_21 = df_21[["Country","Employment", "ConvertedCompYearly","EdLevel","OrgSize","DevType"]]
    df_21 = df_21.rename({"ConvertedCompYearly": "After"}, axis=1)
    
    # education
    df_21 = df_21[df_21["EdLevel"].notnull()]
    df_21['EdLevel'] = df_21['EdLevel'].apply(clean_education)
    df_21 = df_21.rename({"EdLevel": "Education"}, axis=1)
    
    # company size
    df_21 = df_21[df_21["OrgSize"].notnull()]
    df_21['OrgSize'] = df_21['OrgSize'].apply(clean_organization)
    df_21 = df_21.rename({"OrgSize": "Organization"}, axis=1)
    
    # devtype
    country_map = shorten_categories(df_21.DevType.value_counts(), 1)
    df_21["DevType"] = df_21["DevType"].map(country_map)
    df_21 = df_21[df_21["DevType"].notnull()]
    df_21['DevType'] = df_21['DevType'].apply(clean_types)
    df_21 = df_21[df_21["DevType"] != "Other"]

    # CONCAT AFTER CORONA ERA
    df_list_af = [df_20 , df_21]
    df_af = pd.concat(df_list_af)
    df_af = df_af[df_af["After"].notnull()]
    df_af = df_af[df_af["After"] <= 250000]
    df_af = df_af[df_af["After"] >= 10000]
    df_af = df_af[df_af["Employment"] == "Employed full-time"]
    df_af = df_af.drop("Employment", axis=1)

    # FINAL CONCAT
    df_list = [df_af,df_bf]
    df = pd.concat(df_list)
    df['Country'] = df['Country'].apply(clean_country_name)
    country_map = shorten_categories(df.Country.value_counts(), 2000)
    df['Country'] = df['Country'].map(country_map)
    df = df[df["Country"] != "Other"]

    return df

# main page
def show_analysis_page():
    # st, st = st.columns([4, 2])

    st.title('Comparison')

    expander = st.expander("Analysis Through Corona Era")
    eras = ('Before' , 'After' )
    era = expander.multiselect('Pick a year', eras , default='After')
    
    if len(era) > 0 :
        df=load_data_era()
        data = df.groupby(["Country"])[era].mean()
        st.subheader('Analysis of Corona Era -  {}'.format(era))
        st.write("""#### Average salary ($/year) by country """ )
        st.line_chart(data , height=500)
        
        data2 = df.groupby(["Organization"])[era].mean()
        st.write("""#### Average Salary ($/year) based on company size""" )
        st.line_chart(data2 , height=500)
        
        data1 = df.groupby(["Education"])[era].mean()
        st.write("""#### Average Salary ($/year) based on education """ )
        st.line_chart(data1 , height=500)
        
        
        data3 = df.groupby(["DevType"])[era].mean()
        st.write("""#### Average salary ($/year) for developer types""" )
        st.line_chart(data3 , height=500)

    