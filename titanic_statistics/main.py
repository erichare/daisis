import pandas as pd

#load and process data into a global structure
titanic = pd.read_csv("https://raw.githubusercontent.com/pandas-dev/pandas/master/doc/data/titanic.csv")

def mean(field="Age"):
    return float(titanic[field].mean())

def median(field="Age"):
    return float(titanic[field].median())

def percentile(field="Age", percentile=.25):
    return float(titanic[field].quantile(float(percentile)))

def raw(rows: int=5):
    return titanic.head(int(rows))
    
