import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

def load_and_process(d1 = '../data/raw/exams.csv'):
    """ forms a graph between gender and test scores. 
    
    Keyword arguments:
    d1 -- file that we will be looking at (all comes from one file) 
    """
    p = pd.read_csv(d1)

    df1 = (
         pd.read_csv(d1)
        .rename(columns={'gender': 'Sex', 'math score': 'Math Score', 'reading score': 'Reading Score', 'writing score': 'Writing Score'},)
        .dropna()    
    )
    df2 = (
        df1
        .drop(columns = ["race/ethnicity","parental level of education", "test preparation course","lunch"])
        .assign(average=(p['reading score']+p['math score']+p['writing score'])/3)
    )
    return df2
    ...
