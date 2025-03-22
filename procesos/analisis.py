import pandas as pd

class AnalisisDatos:
    def __init__(self, df):
        self.df = df

    def resumen_estadistico(self):
        """Devuelve un resumen estadístico de las columnas numéricas y categóricas."""
        return self.df.describe(include='all')

    def valores_nulos(self):
        """Cuenta los valores nulos por columna y devuelve su ubicación exacta."""
        nulos_por_columna = self.df.isnull().sum()
        ubicaciones_nulos = self.df[self.df.isnull().any(axis=1)].isnull()
        ubicaciones = [(i, col) for i, row in ubicaciones_nulos.iterrows() for col in row.index if row[col]]
        return nulos_por_columna, ubicaciones

    def valores_unicos(self):
        """Devuelve el número de valores únicos por columna."""
        return self.df.nunique()

    def detectar_duplicados(self):
        """Cuenta el número de filas duplicadas en el DataFrame."""
        return self.df.duplicated().sum()

    def correlaciones(self):
        """Calcula la correlación entre columnas numéricas."""
        return self.df.corr()