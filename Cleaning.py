import pandas as pd
import matplotlib.pyplot as plt

# Reading CSV
df = pd.read_csv("Titanic-Dataset.csv")
# Filling Missing Values of Age


def fill_missing_age(df):
    df['Age'].fillna(df['Age'].median(), inplace=True)
    return df


fill_missing_age(df)


# Dropping Cabin Column Since it have too may missing values
def drop_cabin_column(df):
    df.drop(columns=['Cabin'], errors='ignore', inplace=True)
    return df

# Encoding Categorical Columns


def encode_sex(df):
    df['Sex'] = df['Sex'].map({'male': 0, 'female': 1})
    return df


encode_sex(df)
df = pd.get_dummies(df, columns=['Embarked'], drop_first=True)
