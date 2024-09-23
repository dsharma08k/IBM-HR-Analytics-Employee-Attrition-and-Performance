import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def load_cleaned_data(filepath):
    return pd.read_csv(filepath)

def visualize_attrition(df):
    attrition_rate = df['Attrition'].value_counts(normalize=True) * 100
    sns.barplot(x=attrition_rate.index, y=attrition_rate.values)
    plt.title("Attrition Rate")
    plt.xlabel("Attrition")
    plt.ylabel("Percentage")
    plt.tight_layout()
    plt.savefig('C://Users//dsharma08k//Personal//Unified Mentor//IBM HR Analytics Employee Attrition & Performance//results//plots//attrition_rate.png')
    plt.show()

def visualize_features(df):
    sns.histplot(df['Age'], kde=True)
    plt.title('Age Distribution')
    plt.savefig('C://Users//dsharma08k//Personal//Unified Mentor//IBM HR Analytics Employee Attrition & Performance//results//plots//age_distribution.png')
    plt.show()

    sns.countplot(x='Gender', data=df)
    plt.title('Gender Distribution')
    plt.savefig('C://Users//dsharma08k//Personal//Unified Mentor//IBM HR Analytics Employee Attrition & Performance//results//plots//gender_distribution.png')
    plt.show()

if __name__ == "__main__":
    filepath = 'C://Users//dsharma08k//Personal//Unified Mentor//IBM HR Analytics Employee Attrition & Performance//data//employee_attrition_cleaned.csv'
    df = load_cleaned_data(filepath)
    visualize_attrition(df)
    visualize_features(df)
