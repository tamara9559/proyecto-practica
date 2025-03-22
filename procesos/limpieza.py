def limpiar_dataframe(df):
    """Limpia el DataFrame eliminando valores nulos y duplicados.
    Además, permite eliminar columnas sensibles o especificadas por el usuario."""
    if df is not None:
        df = df.dropna().drop_duplicates()
        print("Datos limpiados correctamente.")
        
        # Verificar si hay columnas sensibles
        columnas_sensibles = ["cedula", "direccion"]
        columnas_encontradas = [col for col in columnas_sensibles if col in df.columns]
        
        if columnas_encontradas:
            print(f"Se encontraron columnas sensibles: {', '.join(columnas_encontradas)}")
            for col in columnas_encontradas:
                df.drop(columns=[col], inplace=True)
                print(f"Columna '{col}' eliminada automáticamente.")
        
        # Permitir al usuario eliminar columnas adicionales
        while True:
            print("Columnas disponibles:", list(df.columns))
            columna_a_eliminar = input("Ingrese el nombre de una columna a eliminar (o deje vacío para continuar): ")
            if columna_a_eliminar in df.columns:
                df.drop(columns=[columna_a_eliminar], inplace=True)
                print(f"Columna '{columna_a_eliminar}' eliminada.")
            elif columna_a_eliminar == "":
                break
            else:
                print("Columna no encontrada. Intente nuevamente.")
    
    return df