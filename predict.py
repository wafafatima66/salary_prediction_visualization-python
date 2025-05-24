from itertools import count
import streamlit as st
import pickle
import numpy as np


# def load_model():
#     with open('saved_steps.pkl', 'rb') as file:
#         data = pickle.load(file)
#     return data


# data = load_model()

# regressor = data["model"]
# le_country = data["le_country"]
# le_education = data["le_education"]
# le_gender = data["le_gender"]
# le_devtype = data["le_devtype"]
# le_orgsize = data["le_orgsize"]
# le_Age1stCode = data["le_Age1stCode"]
# le_LearnCode = data["le_LearnCode"]
# le_YearsCode = data["le_YearsCode"]
# le_LanguageHaveWorkedWith = data["le_LanguageHaveWorkedWith"]
# le_DatabaseHaveWorkedWith = data["le_DatabaseHaveWorkedWith"]
# le_PlatformHaveWorkedWith = data["le_PlatformHaveWorkedWith"]
# le_OpSys = data["le_OpSys"]


import joblib

data = joblib.load('saved_steps.joblib')

regressor = data["model"]
le_country = data["le_country"]
le_education = data["le_education"]
le_gender = data["le_gender"]
le_devtype = data["le_devtype"]
le_orgsize = data["le_orgsize"]
le_Age1stCode = data["le_Age1stCode"]
le_LearnCode = data["le_LearnCode"]
le_YearsCode = data["le_YearsCode"]
le_LanguageHaveWorkedWith = data["le_LanguageHaveWorkedWith"]
le_DatabaseHaveWorkedWith = data["le_DatabaseHaveWorkedWith"]
le_PlatformHaveWorkedWith = data["le_PlatformHaveWorkedWith"]
le_OpSys = data["le_OpSys"]


def show_predict_page():
    st.title("IT Professionals Annual Salary ($) Prediction ")
    # st.write("""### We need some information to predict the salary""")


    countries = (
        'United States of America' ,
        'United Kingdom of Great Britain and Northern Ireland',
        'India',
        'South Africa',
        'Germany',
        'France' ,
        'Belgium' ,
        'Australia',
        'Sweden',
        'Netherlands' ,
        'Poland' 
    )

    education = (
        'Master’s degree', 
        'Bachelor’s degree', 
        'Post grad',
        'Less than a Bachelors'
    )

    gender = (
        'Male',
        'Female'
    )
    
    devtype = (
        'Full Stack Developer',
        'Back-End Developer',
        'Front-End Developer',
        'Mobile Developer' ,
        'Developer, desktop or enterprise applications' ,
        'DevOps specialist' ,
        'Developer, embedded applications or devices' ,
        'Engineer, data' ,
        'Engineering manager'  ,
        'Data scientist or machine learning specialist' ,
        # 'Developer, QA or test'  ,
        # 'Academic researcher'   ,
        # 'Senior Executive (C-Suite, VP, etc.)' ,
        # 'Data or business analyst'  
    )
    
    orgsize = (
        'Micro',
        'Small',
        'Medium',
        'Large',
        'Enterprise',
        'Self Employed'
    )
    
    Age1stCode = (
        # 'Younger than 5 years',
        '5 - 10 years' ,
        '11 - 17 years' ,   
        '18 - 24 years' ,
        '25 - 34 years ',
        '35 - 44 years' ,
        # '45 - 54 years ',
        # '55 - 64 years ' ,          
        # 'Older than 64 years'     
    )
    
    learnCode = (
        'School' ,
        'Online resources (Videos , blogs)',
        'Books' ,
        'Online Courses or Certification' ,
        'Online Forum' ,
        'Colleague'  ,
        'Friend or family member',
        'Coding Bootcamp' 
    )
    
    programmingLang = (
        'HTML/CSS' ,
        'JavaScript',
        'SQL' ,
        'TypeScript' ,
        'C#',
        'Node.js' ,
        'PHP' ,
        'Java' ,
        'Python' 
    )
    
    database = (
        'Microsoft SQL Server',
        'MySQL' ,
        'MongoDB' ,
        'MariaDB' ,
        'PostgreSQL' 
    )
    
    platform = (
        'AWS',
        'Google Cloud Platform',
        'Microsoft Azure',
        'Heroku',
        'DigitalOcean' 
    )
    
    operatingSys = (
        'Windows' ,
        'MacOS' ,
        'Linux-based' ,
        'Windows Subsystem for Linux (WSL)'
    )
    
    country = st.selectbox("Country" ,  countries)
    
    education = st.selectbox("Education Level" ,  education)
    
    gender = st.selectbox("Gender" ,  gender)
    
    devtype = st.selectbox("Developer Type" ,  devtype)
    
    orgsize = st.selectbox("Organization Size" ,  orgsize)
    
    Age1stCode = st.selectbox("At what age did you write your first line of code or program" ,  Age1stCode)
    
    learnCode = st.selectbox("How did you learn to code" ,  learnCode)
    
    programmingLang = st.selectbox("Programming Language" ,  programmingLang)
    
    database = st.selectbox("Database" ,  database)
    
    platform = st.selectbox("Platform" ,  platform)
    
    operatingSys = st.selectbox("Operating System" ,  operatingSys)

    if gender == 'Male' :
        gender_select = 'Man'
    elif gender == 'Female' :
        gender_select = 'Woman'

    experience  = st.slider("Years of Professional Experience" , 0,50,3)
    
    years_coding  = st.slider("Years of Coding Experience" , 0,50,3)
    
    ok = st.button("Calculate Salary")
    if ok:
        X = np.array([[country, education, experience , gender_select , devtype , orgsize , Age1stCode , learnCode , years_coding , programmingLang , database , platform , operatingSys]])
        
        X[:, 0] = le_country.transform(X[:,0])
        X[:, 1] = le_education.transform(X[:,1])
        X[:, 3] = le_gender.transform(X[:,3])
        X[:, 4] = le_devtype.transform(X[:,4])
        X[:, 5] = le_orgsize.transform(X[:,5])
        X[:, 6] = le_Age1stCode.transform(X[:,6])
        X[:, 7] = le_LearnCode.transform(X[:,7])
        # X[:, 8] = le_YearsCode.transform(X[:,8])
        X[:, 9] = le_LanguageHaveWorkedWith.transform(X[:,9])
        X[:, 10] = le_DatabaseHaveWorkedWith.transform(X[:,10])
        X[:, 11] = le_PlatformHaveWorkedWith.transform(X[:,11])
        X[:, 12] = le_OpSys.transform(X[:,12])
        
        X = X.astype(float)

        salary = regressor.predict(X)
        st.subheader(f"The estimated salary is ${salary[0]:.2f}")