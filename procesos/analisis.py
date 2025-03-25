import pandas as pd

class AnalisisDatos:
    def __init__(self, df):
        self.df = df.replace(r'^\s*$', pd.NA, regex=True)  # Convierte espacios vacíos en NaN

    def valores_nulos(self):
        """Cuenta los valores nulos por columna y en toda la tabla."""
        nulos_por_columna = self.df.isnull().sum()
        total_nulos = nulos_por_columna.sum()
        return nulos_por_columna, total_nulos

    def estadisticas_descriptivas(self):
        """Calcula medidas estadísticas dependiendo del tipo de dato."""
        resultados = {}

        for columna in self.df.columns:
            if pd.api.types.is_numeric_dtype(self.df[columna]):
                resultados[columna] = {
                    'Media': self.df[columna].mean(),
                    'Mediana': self.df[columna].median(),
                    'Moda': self.df[columna].mode().tolist(),
                    'Varianza': self.df[columna].var(),
                    'Desviación Estándar': self.df[columna].std()
                }
            elif pd.api.types.is_object_dtype(self.df[columna]):
                resultados[columna] = self.df[columna].value_counts().head(5).to_dict()

        return resultados


