import streamlit as st
import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt
from my_function import shorten_categories
from my_function import clean_experience
from my_function import clean_education
from my_function import clean_country_name
from my_function import clean_experience_2018
from my_function import clean_organization
from my_function import clean_types
from my_function import clean_types_18

@st.cache_data
def load_data(year):
    
    df = pd.read_csv("./data/"+year+".csv")

    if year == '2021':
        df = df[["Country","Employment", "ConvertedCompYearly","Gender" , "YearsCodePro", "EdLevel" , "OrgSize" , "DevType"]]
        
        df = df[df["ConvertedCompYearly"].notnull()]
        df = df[df["YearsCodePro"].notnull()]
        df = df[df["Gender"].notnull()]
        df = df[df["EdLevel"].notnull()]
        df = df[df["OrgSize"].notnull()]
        
        df = df.loc[df['Gender'].isin(['Man','Woman'])]
        
        df["YearsCodePro"] = df["YearsCodePro"].apply(clean_experience)
        df = df[df["ConvertedCompYearly"].notnull()]
        df = df[df["ConvertedCompYearly"] <= 250000]
        df = df[df["ConvertedCompYearly"] >= 10000]
        df['Country'] = df['Country'].apply(clean_country_name)
        country_map = shorten_categories(df.Country.value_counts(), 1000)
        df["Country"] = df["Country"].map(country_map)
        df = df[df["Country"] != "Other"]
        df = df[df["Employment"] == "Employed full-time"]
        
        df['EdLevel'] = df['EdLevel'].apply(clean_education)
        df['OrgSize'] = df['OrgSize'].apply(clean_organization)
        
        country_map = shorten_categories(df.DevType.value_counts(), 1)
        df["DevType"] = df["DevType"].map(country_map)
        df = df[df["DevType"].notnull()]
        df['DevType'] = df['DevType'].apply(clean_types)
        df = df[df["DevType"] != "Other"]
        
        df_male = df.loc[df['Gender'].isin(['Man'])]
        df_male = df_male.rename({"ConvertedCompYearly": "Man"}, axis=1)

        df_female = df.loc[df['Gender'].isin(['Woman'])]
        df_female = df_female.rename({"ConvertedCompYearly": "Woman"}, axis=1)

        df_list_af = [df_male , df_female]
        df = pd.concat(df_list_af)

        df = df.drop("Employment", axis=1)
        df = df.drop("Gender", axis=1)

    elif year == '2020':
        df = df[["Country","Employment", "ConvertedComp","Gender" , "YearsCodePro" ,"EdLevel","OrgSize","DevType"]]
        
        df = df[df["ConvertedComp"].notnull()]
        df = df[df["YearsCodePro"].notnull()]
        df = df[df["Gender"].notnull()]
        df = df[df["OrgSize"].notnull()]
        
        df = df.loc[df['Gender'].isin(['Man','Woman'])]
        df["YearsCodePro"] = df["YearsCodePro"].apply(clean_experience)
        
        df = df[df["EdLevel"].notnull()]
        df['EdLevel'] = df['EdLevel'].apply(clean_education)
        
        df['OrgSize'] = df['OrgSize'].apply(clean_organization)
        
        # devtype
        country_map = shorten_categories(df.DevType.value_counts(), 1)
        df["DevType"] = df["DevType"].map(country_map)
        df = df[df["DevType"].notnull()]
        df['DevType'] = df['DevType'].apply(clean_types)
        df = df[df["DevType"] != "Other"]
        
        df_male = df.loc[df['Gender'].isin(['Man'])]
        df_male = df_male.rename({"ConvertedComp": "Man"}, axis=1)

        df_female = df.loc[df['Gender'].isin(['Woman'])]
        df_female = df_female.rename({"ConvertedComp": "Woman"}, axis=1)

        df_list_af = [df_male , df_female]
        df_gender = pd.concat(df_list_af)

        df_gender['Country'] = df_gender['Country'].apply(clean_country_name)
        country_map = shorten_categories(df_gender.Country.value_counts(), 700)
        df_gender["Country"] = df_gender["Country"].map(country_map)
        df = df_gender[df_gender["Country"] != "Other"]

        df = df[df["Employment"] == "Employed full-time"]
        df = df.drop("Employment", axis=1)
        df = df.drop("Gender", axis=1)
        
    elif year == '2019':
      
        df = df[["Country","Employment", "ConvertedComp","Gender" , "YearsCodePro" ,"EdLevel","OrgSize","DevType"]]
        
        df = df[df["ConvertedComp"].notnull()]
        df = df[df["YearsCodePro"].notnull()]
        df = df[df["Gender"].notnull()]
        df = df[df["OrgSize"].notnull()]
        
        df = df.loc[df['Gender'].isin(['Man','Woman'])]
        df["YearsCodePro"] = df["YearsCodePro"].apply(clean_experience)
        
        df = df[df["EdLevel"].notnull()]
        df['EdLevel'] = df['EdLevel'].apply(clean_education)
        
        df['OrgSize'] = df['OrgSize'].apply(clean_organization)
        
        # devtype
        country_map = shorten_categories(df.DevType.value_counts(), 1)
        df["DevType"] = df["DevType"].map(country_map)
        df = df[df["DevType"].notnull()]
        df['DevType'] = df['DevType'].apply(clean_types)
        df = df[df["DevType"] != "Other"]
        
        df_male = df.loc[df['Gender'].isin(['Man'])]
        df_male = df_male.rename({"ConvertedComp": "Man"}, axis=1)

        df_female = df.loc[df['Gender'].isin(['Woman'])]
        df_female = df_female.rename({"ConvertedComp": "Woman"}, axis=1)

        df_list_af = [df_male , df_female]
        df_gender = pd.concat(df_list_af)

        df_gender['Country'] = df_gender['Country'].apply(clean_country_name)
        country_map = shorten_categories(df_gender.Country.value_counts(), 1000)
        df_gender["Country"] = df_gender["Country"].map(country_map)
        df = df_gender[df_gender["Country"] != "Other"]

        df = df[df["Employment"] == "Employed full-time"]
        df = df.drop("Employment", axis=1)
        df = df.drop("Gender", axis=1)

    elif year == '2018' :
        
        df = pd.read_csv("./data/2018.csv")
        df = df[["Country","Employment", "ConvertedSalary","Gender" , "YearsCodingProf" ,"FormalEducation" , "CompanySize" , "DevType"]]
        df = df[df["ConvertedSalary"].notnull()]
        df = df[df["YearsCodingProf"].notnull()]
        df = df[df["CompanySize"].notnull()]
        
        df["YearsCodingProf"] = df["YearsCodingProf"].apply(clean_experience_2018)
        df= df.rename({"YearsCodingProf": "YearsCodePro"}, axis=1)
        df = df[df["Gender"].notnull()]
        df = df.loc[df['Gender'].isin(['Male','Female'])]
        
      
        df = df[df["FormalEducation"].notnull()]
        df['FormalEducation'] = df['FormalEducation'].apply(clean_education)
        
        df['CompanySize'] = df['CompanySize'].apply(clean_organization)

        #  dev type
        country_map = shorten_categories(df.DevType.value_counts(), 1)
        df["DevType"] = df["DevType"].map(country_map)
        df = df[df["DevType"].notnull()]
        df['DevType'] = df['DevType'].apply(clean_types_18)
        df = df[df["DevType"] != "Other"]
        
        df_male = df.loc[df['Gender'].isin(['Male'])]
        df_male = df_male.rename({"ConvertedSalary": "Male"}, axis=1)

        df_female = df.loc[df['Gender'].isin(['Female'])]
        df_female = df_female.rename({"ConvertedSalary": "Female"}, axis=1)

        df_list_af = [df_male , df_female]
        df_gender = pd.concat(df_list_af)

        df_gender['Country'] = df_gender['Country'].apply(clean_country_name)
        country_map = shorten_categories(df_gender.Country.value_counts(), 700)
        df_gender["Country"] = df_gender["Country"].map(country_map)
        df = df_gender[df_gender["Country"] != "Other"]

        df = df[df["Employment"] == "Employed full-time"]
        df = df.drop("Employment", axis=1)
        df = df.drop("Gender", axis=1)


    return df


def show_report_page():

    expander = st.expander("Select Year")
    year = expander.selectbox(
        "",
        ('2021', '2020', '2019','2018'))
    
    st.title('Report of {}'.format(year))
    
    col1, col2 = st.columns([4, 4])


    if year == '2018' :
            df = load_data(year)
            col1.write("""#### Average salary ($/year) by country """ )
            data = df.groupby(["Country"])["Male","Female"].mean()
            col1.line_chart(data , height=500)
            
            col1.write("""#### Average Salary ($/year) based on education  """ )
            data = df.groupby(["FormalEducation"])["Male","Female"].mean()
            col1.line_chart(data , height=500)
         
            col2.write("""#### Average Salary ($/year) based on company size""" )
            data = df.groupby(["CompanySize"])["Male","Female"].mean()
            col2.line_chart(data , height=500)
            
            col2.write("""#### Average salary ($/year) for developer types""" )
            data = df.groupby(["DevType"])["Male","Female"].mean()
            col2.line_chart(data , height=500)
            
    else :
            df = load_data(year)
            col1.write("""#### Average salary ($/year) by country """ )
            # data = df.groupby(["Country"])["Man","Woman"].mean()
            data = df.groupby(["Country"])[["Man", "Woman"]].mean()
            col1.line_chart(data , height=500)
            
            col1.write("""#### Average Salary ($/year) based on education  """ )
            # data = df.groupby(["EdLevel"])["Man","Woman"].mean()
            data = df.groupby(["EdLevel"])[["Man", "Woman"]].mean()
            col1.line_chart(data , height=500)
            
            col2.write("""#### Average Salary ($/year) based on company size """ )
            # data = df.groupby(["OrgSize"])["Man","Woman"].mean()
            data = df.groupby(["OrgSize"])[["Man", "Woman"]].mean()
            col2.line_chart(data , height=500)
            
            col2.write("""#### Average salary ($/year) for developer types""" )
            # data = df.groupby(["DevType"])["Man","Woman"].mean()
            data = df.groupby(["DevType"])[["Man", "Woman"]].mean()
            col2.line_chart(data , height=500)
            
