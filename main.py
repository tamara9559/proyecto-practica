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

    print("\n📊 Estadísticas Descriptivas:")
    estadisticas = analisis.estadisticas_descriptivas()
    for columna, valores in estadisticas.items():
        print(f"\n🔹 {columna}:")
        for clave, valor in valores.items():
            print(f"  {clave}: {valor}")

    # 4️⃣ Visualización de datos
    visualizador = VisualizacionDatos(df)
    visualizador.graficar_valores_nulos()
    visualizador.graficar_estadisticas_numericas()
    visualizador.graficar_frecuencia_categorias()

    print("\n✅ Análisis y visualización completados.")

if __name__ == "__main__":
    main()
