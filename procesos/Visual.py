import os
import matplotlib.pyplot as plt
import seaborn as sns
import re

class VisualizacionDatos:
    """
    Clase para generar y guardar visualizaciones de un DataFrame.
    
    Métodos:
    - graficar_valores_nulos(): Grafica valores nulos en cada columna.
    - graficar_estadisticas_numericas(): Grafica estadísticas clave de variables numéricas.
    - graficar_frecuencia_categorias(): Genera gráficos de pastel para las categorías más repetidas.
    """

    def __init__(self, df):
        """
        Inicializa la clase con un DataFrame y crea la carpeta 'resultados' si no existe.
        
        :param df: DataFrame de pandas con los datos a visualizar.
        """
        self.df = df
        self.carpeta_resultados = "resultados"
        os.makedirs(self.carpeta_resultados, exist_ok=True)

    def guardar_grafica(self, nombre_archivo):
        """
        Guarda la gráfica actual en la carpeta 'resultados' con un nombre válido.
        
        :param nombre_archivo: Nombre del archivo a guardar.
        """
        nombre_archivo = re.sub(r'[<>:"/\\|?*\n]+', '_', nombre_archivo)  # Reemplaza caracteres inválidos
        ruta_completa = os.path.join(self.carpeta_resultados, nombre_archivo)
        plt.savefig(ruta_completa)
        print(f"✅ Gráfica guardada en: {ruta_completa}")
        plt.close()

    def graficar_valores_nulos(self):
        """
        Muestra y guarda un gráfico de barras con la cantidad de valores nulos en cada columna.
        """
        nulos_por_columna = self.df.isnull().sum()
        
        if nulos_por_columna.sum() == 0:
            print("✅ No hay valores nulos en el DataFrame.")
            return
        
        plt.figure(figsize=(10, 5))
        nulos_por_columna.plot(kind='bar', color='red', alpha=0.7)
        plt.title('Valores nulos por columna')
        plt.xlabel('Columnas')
        plt.ylabel('Cantidad de valores nulos')
        self.guardar_grafica("valores_nulos_barras.png")

    def graficar_estadisticas_numericas(self):
        """
        Genera gráficos de línea para variables numéricas, mostrando media, mediana y moda.
        """
        df_numerico = self.df.select_dtypes(include=['number'])
        
        if df_numerico.empty:
            print("⚠️ No hay datos numéricos para graficar.")
            return
        
        for columna in df_numerico.columns:
            plt.figure(figsize=(10, 5))
            plt.plot(df_numerico[columna], label="Valores", color="blue")
            plt.axhline(df_numerico[columna].mean(), color="red", linestyle="--", label="Media")
            plt.axhline(df_numerico[columna].median(), color="green", linestyle="--", label="Mediana")
            
            # Verificar si la moda está definida
            moda = df_numerico[columna].mode()
            if not moda.empty:
                plt.axhline(moda.iloc[0], color="purple", linestyle="--", label="Moda")
            
            plt.title(f"Distribución de {columna}")
            plt.legend()
            self.guardar_grafica(f"{columna}_estadisticas.png")

    def graficar_frecuencia_categorias(self):
        """
        Genera gráficos de pastel para las 5 categorías más frecuentes en columnas de tipo texto.
        """
        df_categorico = self.df.select_dtypes(include=['object'])
        
        if df_categorico.empty:
            print("⚠️ No hay datos categóricos para graficar.")
            return
        
        for columna in df_categorico.columns:
            top_5 = df_categorico[columna].value_counts().head(5)
            if top_5.empty:
                continue
            
            plt.figure(figsize=(8, 8))
            top_5.plot(kind='pie', autopct='%1.1f%%', colors=sns.color_palette("pastel"))
            plt.title(f"Top 5 valores más repetidos en {columna}")
            self.guardar_grafica(f"{columna}_top5_pastel.png")

