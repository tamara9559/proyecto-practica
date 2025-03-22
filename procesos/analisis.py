def analizar_dataframe(df):
    """Realiza un análisis básico de los datos."""
    if df is not None:
        print("Resumen estadístico:")
        print(df.describe())
        print("\nValores nulos por columna:")
        print(df.isnull().sum())