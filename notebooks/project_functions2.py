import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

d = '../data/raw/exams.csv'
def load_and_process(d):
    d1 = pd.read_csv('../data/raw/exams.csv')
    df1 = (
        pd.read_csv(d)
        .rename(columns={'gender': 'Sex', 'math score': 'Math Score', 'reading score': 'Reading Score', 'writing score': 'Writing Score'},)
        .dropna()    
    )
    df2 = (
        df1
        .drop(columns = ["race/ethnicity","parental level of education", "test preparation course","lunch"])
        .assign(total=(d1['reading score'])+(d1['math score'])+(d1['writing score']))
        .assign(total = total) 
     )
    return df2
print(load_and_process(d))