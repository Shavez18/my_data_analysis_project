import pandas as pd

def clean_data(df):
    """Simple data cleaning function"""
    df = df.dropna()
    df = df.reset_index(drop=True)
    return df

if __name__ == "__main__":
    print("Data cleaning script ready!")
