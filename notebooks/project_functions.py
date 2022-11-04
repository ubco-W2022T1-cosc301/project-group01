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
              .assign(total=d.iloc[:,[2,3,4]].sum(axis=1))
    )
    return finished