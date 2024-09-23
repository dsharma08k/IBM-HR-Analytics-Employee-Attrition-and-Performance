import pandas as pd

def load_data(filepath):
    return pd.read_csv(filepath)

def clean_data(df):
    df.drop_duplicates(inplace=True)
    
    missing_values = df.isnull().sum()
    
    return df, missing_values

def save_cleaned_data(df, filepath):
    df.to_csv(filepath, index=False)

if __name__ == "__main__":
    filepath = 'C://Users//dsharma08k//Personal//Unified Mentor//IBM HR Analytics Employee Attrition & Performance//data//employee_attrition.csv'
    df = load_data(filepath)
    df_cleaned, missing_vals = clean_data(df)
    print(f"Missing values:\n{missing_vals}")
    save_cleaned_data(df_cleaned, 'C://Users//dsharma08k//Personal//Unified Mentor//IBM HR Analytics Employee Attrition & Performance//data//employee_attrition_cleaned.csv')
