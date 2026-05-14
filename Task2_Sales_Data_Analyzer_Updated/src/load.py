import pandas as pd

def load(file):
    df = pd.read_csv(file)
    return df