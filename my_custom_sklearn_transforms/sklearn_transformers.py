from sklearn.base import BaseEstimator, TransformerMixin


# All sklearn Transforms must have the `transform` and `fit` methods
class DropColumns(BaseEstimator, TransformerMixin):
    def __init__(self, columns):
        self.columns = columns

    def fit(self, X, y=None):
        return self
    
    def transform(self, X):
        # Primeiro realizamos a cópia do dataframe 'X' de entrada
        data = X.copy()
        # Retornamos um novo dataframe sem as colunas indesejadas
        return data.drop(labels=self.columns, axis='columns')

class SplitColumns(BaseEstimator, TransformerMixin):
    def __init__(self, columns):
        self.columns = columns

    def fit(self, X, y=None):
        return self
    
    def transform(self, X):
        # Primeiro realizamos a cópia do dataframe 'X' de entrada
        data = X.copy()
        # Retornamos um novo dataframe sem as colunas indesejadas
        for col in self.columns:
            min_ = data[col].min()
            max_ = data[col].max()
            for i in range(min_, max_ + 1):
                data['{}_{}'.format(i, col)] = (data[col] == i).apply(int)
                data['{}_{}'.format(i, col)] = (data[col] == i).apply(int)
                data['{}_{}'.format(i, col)] = (data[col] == i).apply(int)
        return data.drop(columns=self.columns)
