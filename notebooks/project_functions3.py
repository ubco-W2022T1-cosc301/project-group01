import pandas as pd
def load_and_process(urlOrPath):
    """
    loads and processes data given a path parameter.
    returns a dataset of a cleaned up dataset"""
    dataF = (
        pd.read_csv(urlOrPath)
        .dropna()
    )
    finished=(dataF
              .drop(columns = ['gender','lunch','parental level of education'])
              .assign(total=dataF.iloc[:,[5,6,7]].sum(axis=1))
    )
    return finished