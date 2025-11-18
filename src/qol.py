import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from src.types import QOLColumns as QC

# Columns to normalize (all except QOL Index and City)
positive_normalized_columns = { QC.PPI, QC.SI, QC.HC, QC.CI }
negative_normalized_columns = { QC.COL, QC.PPIR, QC.TCT, QC.PI }
columns_to_normalize = positive_normalized_columns.union(negative_normalized_columns)

def quantile_normalize(df: pd.DataFrame, columns):
    """
    Perform quantile normalization on specified columns
    """
    # Extract the data to normalize
    data_to_normalize = df[columns].copy()
    
    # Sort each column
    sorted_data = np.sort(data_to_normalize, axis=0)
    
    # Calculate rank means
    rank_means = sorted_data.mean(axis=1)
    
    # Get ranks for each column
    ranks = data_to_normalize.rank(method='average').astype(int) - 1
    
    # Replace values with rank means
    normalized_data = pd.DataFrame(
        np.array([rank_means[ranks[col].values] for col in columns]).T,
        columns=columns,
        index=df.index
    )
    
    return normalized_data

def get_qol(df: pd.DataFrame):
    df = quantile_normalize(df, list(columns_to_normalize))
    return 100 + df[list(positive_normalized_columns)].sum(axis=1) - df[list(negative_normalized_columns)].sum(axis=1)
