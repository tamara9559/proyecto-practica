import pandas as pd
from procesos.CargueDatos import CargueDatos
from procesos.Limpieza import Limpieza
from procesos.Analisis import AnalisisDatos
from procesos.Visual import VisualizacionDatos

import sys
sys.dont_write_bytecode = True

def main():
    print("📊 Cargador de Datos")

    # 1️⃣ Cargar datos
    cargador = CargueDatos()
    df = cargador.cargar_datos()

    if df is None:
        print("❌ No se cargaron datos. Terminando ejecución.")
        return

    # 2️⃣ Limpiar los datos
    limpieza = Limpieza(df)
    df = limpieza.ejecutar_limpeza()

    # 3️⃣ Analizar los datos
    analisis = AnalisisDatos(df)

    print("\n❌ Valores Nulos:")
    nulos, total_nulos = analisis.valores_nulos()
    print("Valores nulos por columna:\n", nulos)
    print(f"Total de valores nulos en la tabla: {total_nulos}")

    # 4️⃣ Visualización de datos
    visualizador = VisualizacionDatos(df)
    visualizador.graficar_valores_nulos()
    visualizador.graficar_histogramas()
    visualizador.graficar_boxplots()
    visualizador.graficar_matriz_correlacion()
    visualizador.graficar_valores_categoricos()

    print("\n✅ Análisis y visualización completados.")

if __name__ == "__main__":
    main()
