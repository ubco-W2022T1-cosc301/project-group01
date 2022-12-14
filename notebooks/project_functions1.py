import pandas as pd
import numpy as np
import seaborn as sns

def load_and_process(df ='../data/raw/exams.csv'):
    '''
    This is the load and process fucntion built by Noah Stasuik
    
    In this function for my data analysis I drop the columns that are not needed, create new columns to help with my research, and clean any data that is   not needed in the dataset.
    '''
    df1 = pd.read_csv(df)
    df2 = (
        pd.read_csv(df)
        .drop(columns = ['gender','lunch','race/ethnicity', 'test preparation course'])
        .assign(average_score = round((df1['math score'] + df1['reading score'] + df1['writing score']) /3, 2))
        .dropna()  
        .assign(parental_education_n = df1['parental level of education'].replace(['some high school', 'high school', 'some college', 'associate\'s degree', 'bachelor\'s degree', 'master\'s degree'], [1, 2, 3, 4, 5, 6]))
    )
    return df2