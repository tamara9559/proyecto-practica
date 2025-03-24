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

    def detectar_duplicados(self):
        """Cuenta el número de filas duplicadas en el DataFrame."""
        return self.df.duplicated().sum()
    
    def medidas_tendencia_central(self):
        """Calcula media, mediana y moda de las columnas numéricas."""
        medidas = {
         'Media': self.df.mean(numeric_only=True),
         'Mediana': self.df.median(numeric_only=True),
         'Moda': {col: list(self.df[col].mode().values) for col in self.df.select_dtypes(include=['number']).columns}
    }
        return medidas

    
    def medidas_dispersion(self):
        """Calcula rango, varianza, desviación estándar y coeficiente de variación."""
        dispersion = {
            'Rango': self.df.max(numeric_only=True) - self.df.min(numeric_only=True),
            'Varianza': self.df.var(numeric_only=True),
            'Desviación Estándar': self.df.std(numeric_only=True),
            'Coeficiente de Variación': self.df.std(numeric_only=True) / self.df.mean(numeric_only=True)
        }
        return dispersion

