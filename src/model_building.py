from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report
from sklearn.model_selection import train_test_split
import pandas as pd

def load_cleaned_data(filepath):
    return pd.read_csv(filepath)

def prepare_data(df):
    df_dummies = pd.get_dummies(df, drop_first=True)
    
    X = df_dummies.drop(columns=['Attrition_Yes'])
    y = df_dummies['Attrition_Yes']  
    
    return X, y

def train_model(X_train, y_train):
    model = RandomForestClassifier(random_state=42, class_weight='balanced')
    model.fit(X_train, y_train)
    return model

def evaluate_model(model, X_test, y_test):
    predictions = model.predict(X_test)
    print(classification_report(y_test, predictions))

if __name__ == "__main__":
    filepath = 'C://Users//dsharma08k//Personal//Unified Mentor//IBM HR Analytics Employee Attrition & Performance//data//employee_attrition_cleaned.csv'
    df = load_cleaned_data(filepath)
    X, y = prepare_data(df)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
    model = train_model(X_train, y_train)
    evaluate_model(model, X_test, y_test)
