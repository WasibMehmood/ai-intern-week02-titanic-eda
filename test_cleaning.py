import pandas as pd
from Cleaning import fill_missing_age, drop_cabin_column, encode_sex


def test_fill_missing_age():
    df = pd.DataFrame({'Age': [22, None, 24, None]})
    result = fill_missing_age(df.copy())
    assert result['Age'].isna().sum() == 0
    assert all(result['Age'].notna())


def test_drop_cabin_column():
    df = pd.DataFrame({'A': [1], 'Cabin': ['C85']})
    result = drop_cabin_column(df.copy())
    assert 'Cabin' not in result.columns


def test_encode_sex():
    df = pd.DataFrame({'Sex': ['male', 'female', 'male']})
    result = encode_sex(df.copy())
    assert set(result['Sex'].unique()) <= {0, 1}
    assert set(result['Sex'].unique()) <= {0, 1}
