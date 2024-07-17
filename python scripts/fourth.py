''' code that uses pandas and creates a Python function to clean and preprocess a given 
DataFrame, which involves handling missing values, normalizing numerical columns, and encoding 
categorical columns.'''
import pandas as pd
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.impute import SimpleImputer
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline

def clean_and_preprocess(df):
    target = None
    if 'target' in df.columns:
        target = df['target']
        df = df.drop('target', axis=1)
    numerical_cols = df.select_dtypes(include=['int64', 'float64']).columns
    categorical_cols = df.select_dtypes(include=['object', 'category']).columns
    numerical_transformer = Pipeline(steps=[
        ('imputer', SimpleImputer(strategy='mean')),
        ('scaler', StandardScaler())
    ])
    
    categorical_transformer = Pipeline(steps=[
        ('imputer', SimpleImputer(strategy='most_frequent')),
        ('onehot', OneHotEncoder(handle_unknown='ignore'))
    ])
    preprocessor = ColumnTransformer(
        transformers=[
            ('num', numerical_transformer, numerical_cols),
            ('cat', categorical_transformer, categorical_cols)
        ])
    df_cleaned = preprocessor.fit_transform(df)
    df_cleaned = pd.DataFrame(df_cleaned, columns=preprocessor.get_feature_names_out())
    if target is not None:
        df_cleaned['target'] = target.reset_index(drop=True)
    
    return df_cleaned
data = {
    'age': [25, 30, 35, None, 40],
    'salary': [50000, 60000, None, 80000, 100000],
    'city': ['New York', 'Los Angeles', 'New York', None, 'Los Angeles'],
    'target': [1, 0, 1, 0, 1]
}
df = pd.DataFrame(data)

cleaned_df = clean_and_preprocess(df)
print(cleaned_df)

