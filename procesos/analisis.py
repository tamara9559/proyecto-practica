import pandas as pd

class AnalisisDatos:
    """
    Clase para realizar análisis estadístico de un DataFrame.
    
    Métodos:
    - valores_nulos(): Cuenta los valores nulos en cada columna y en todo el DataFrame.
    - estadisticas_descriptivas(): Genera estadísticas según el tipo de dato de cada columna.
    """

    def __init__(self, df):
        """
        Inicializa la clase con un DataFrame y reemplaza espacios vacíos con NaN.
        
        :param df: DataFrame de pandas a analizar.
        """
        self.df = df.replace(r'^\s*$', pd.NA, regex=True)  # Convierte espacios vacíos en NaN

    def valores_nulos(self):
        """
        Cuenta los valores nulos en cada columna y el total en el DataFrame.
        
        :return: (Series, int) -> Serie con nulos por columna y total general.
        """
        nulos_por_columna = self.df.isnull().sum()
        total_nulos = nulos_por_columna.sum()
        return nulos_por_columna, total_nulos

    def estadisticas_descriptivas(self):
        """
        Calcula estadísticas descriptivas dependiendo del tipo de dato de cada columna.
        
        - Para columnas numéricas: Media, Mediana, Moda, Varianza y Desviación Estándar.
        - Para columnas categóricas: Los 5 valores más frecuentes.

        :return: Diccionario con estadísticas por columna.
        """
        resultados = {}

        for columna in self.df.columns:
            if pd.api.types.is_numeric_dtype(self.df[columna]):  # Si es numérica
                resultados[columna] = {
                    'Media': self.df[columna].mean(),
                    'Mediana': self.df[columna].median(),
                    'Moda': self.df[columna].mode().tolist(),
                    'Varianza': self.df[columna].var(),
                    'Desviación Estándar': self.df[columna].std()
                }
            elif pd.api.types.is_object_dtype(self.df[columna]):  # Si es categórica
                resultados[columna] = self.df[columna].value_counts().head(5).to_dict()

        return resultados



