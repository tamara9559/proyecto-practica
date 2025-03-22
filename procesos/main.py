from cargar_datos import cargar_excel
from limpieza import limpiar_dataframe
from analisis import analizar_dataframe
from visual import generar_graficos

if __name__ == "__main__":
    ruta = "datos.xlsx"
    df = cargar_excel(ruta)
    df = limpiar_dataframe(df)
    analizar_dataframe(df)
    generar_graficos(df)
