import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

d1 = pd.read_csv('../data/raw/exams.csv')
def load_and_process(d1):
    """ forms a graph between gender and test scores. 
    
    Keyword arguments:
    d1 -- file that we will be looking at (all comes from one file) 
    """
    df1 = (
         d = pd.read_csv(d1)
        .rename(columns={'gender': 'Sex', 'math score': 'Math Score', 'reading score': 'Reading Score', 'writing score': 'Writing Score'},)
        .dropna()    
    )
    df2 = (
        df1
        .drop(columns = ["race/ethnicity","parental level of education", "test preparation course","lunch"])
        .assign(average=(d['reading score']+d['math score']+d['writing score'])/3)
    )
    return df2
    ...
