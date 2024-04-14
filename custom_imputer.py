from sklearn.base import BaseEstimator, TransformerMixin
import pandas as pd

class CustomImputer(BaseEstimator, TransformerMixin):
    def __init__(self, strategy='mean', custom_value=None):
        self.strategy = strategy
        self.custom_value = custom_value
    
    def fit(self, X, y=None):
        if self.strategy == 'mean':
            self.custom_values = X.mean()
        elif self.strategy == 'median':
            self.custom_values = X.median()
        elif self.strategy == 'mode':
            self.custom_values = X.mode().iloc[0]  # Take the first mode if multiple modes exist
        elif self.strategy == 'constant':
            if self.custom_value is None:
                raise ValueError("Custom value must be provided for constant imputation strategy")
            self.custom_values = pd.Series(self.custom_value, index=X.columns)
        else:
            raise ValueError("Invalid strategy. Please choose from 'mean', 'median', 'mode', or 'constant'")
        return self
    
    def transform(self, X):
        # Apply custom imputation to the input data
        X_imputed = X.fillna(self.custom_values)
        return X_imputed
