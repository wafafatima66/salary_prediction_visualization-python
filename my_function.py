def clean_country_name(x):
    if x ==  'United States of America':
        return 'United States'
    if x == 'United Kingdom of Great Britain and Northern Ireland':
        return 'United Kingdom'
    return x

def shorten_categories(categories, cutoff):
    categorical_map = {}
    for i in range(len(categories)):
        if categories.values[i] >= cutoff:
            categorical_map[categories.index[i]] = categories.index[i]
        else:
            categorical_map[categories.index[i]] = 'Other'
    return categorical_map

def clean_experience(x):
    if x ==  'More than 50 years':
        return 50
    if x == 'Less than 1 year':
        return 0.5
    return float(x)

def clean_education(x):
    if 'Bachelor’s degree' in x:
        return 'Bachelor’s degree'
    if 'Master’s degree' in x:
        return 'Master’s degree'
    if 'Professional degree' in x or 'Other doctoral' in x:
        return 'Post grad'
    return 'Less than a Bachelors'

def clean_experience_2018(x):
    if x ==  '3-5 years':
        return 4
    if x == '18-20 years':
        return 19
    if x == '6-8 years':
        return 7
    if x == '12-14 years':
        return 13
    if x == '0-2 years':
        return 1
    if x == '21-23 years':
        return 22
    if x == '24-26 years':
        return 25
    if x == '9-11 years':
        return 10
    if x == '15-17 years':
        return 16
    if x == '27-29 years':
        return 28
    if x == '30 or more years':
        return 50
    return float(x)

def clean_organization(x):
    if '2 to 9 employees' in x or '10 to 19 employees' in x or 'Fewer than 10 employees' in x:
        return 'Micro'
    if '100 to 499 employees' in x or '20 to 99 employees' in x :
        return 'Small'
    if '500 to 999 employees' in x  :
        return 'Medium'
    if '1,000 to 4,999 employees' in x:
        return 'Large'
    if '10,000 or more employees' in x or '5,000 to 9,999 employees' in x:
        return 'Enterprise'
    return 'Self Employed'

def clean_types(x):
    if 'Developer, full-stack'  in x or 'Developer, front-end;Developer, full-stack;Developer, back-end' in x or 'Developer, back-end;Developer, front-end;Developer, full-stack' in x:
        return 'Full Stack Developer'
    if 'Developer, back-end' in x or 'Developer, full-stack;Developer, back-end' in x or 'Developer, back-end;Developer, full-stack' in x:
        return 'Back-End Developer'
    if 'Developer, front-end' in x  or 'Developer, front-end;Developer, full-stack' in x:
        return 'Front-End Developer'
    if 'Developer, mobile ' in x:
        return 'Mobile Developer'
    if 'Student' in x:
        return 'Student'
    return 'Other'

def clean_types_18(x):
    if 'Full-stack developer' in x or 'Back-end developer;Front-end developer;Full-stack developer' in x:
        return 'Full Stack Developer'
    if 'Back-end developer' in x:
        return 'Back-End Developer'
    if 'Developer, front-end' in x  or 'Developer, front-end;Developer, full-stack' in x:
        return 'Front-End Developer'
    if 'Mobile developer' in x:
        return 'Mobile Developer'
    if 'Student' in x:
        return 'Student'
    return 'Other'

def clean_types_comparison(x):
    if 'Full-stack developer' in x or 'Back-end developer;Front-end developer;Full-stack developer' in x:
        return 'Full Stack Developer'
    if 'Back-end developer' in x:
        return 'Back-End Developer'
    if 'Developer, front-end' in x  or 'Developer, front-end;Developer, full-stack' in x:
        return 'Front-End Developer'
    return 'Other'