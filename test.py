import langchain

#import pandas as pd

def preprocess_data(df):
    # Step 1: Drop missing values
    df = df.dropna()
    
    # Step 2: Convert 'Name' column to lowercase
    df['Name'] = df['Name'].str.lower()
    
    # Step 3: Cap outliers in the 'Age' column
    df['Age'][df['Age'] > 100] = 100
    
    return df