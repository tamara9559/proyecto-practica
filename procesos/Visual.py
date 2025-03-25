import os
import matplotlib.pyplot as plt
import seaborn as sns
import re


class VisualizacionDatos:
    def __init__(self, df):
        self.df = df
        self.carpeta_resultados = "resultados"
        os.makedirs(self.carpeta_resultados, exist_ok=True)

    def guardar_grafica(self, nombre_archivo):
        """Guarda la gráfica en la carpeta 'resultados', asegurando que el nombre del archivo sea válido."""
        nombre_archivo = re.sub(r'[<>:"/\\|?*\n]+', '_', nombre_archivo)  # Reemplaza caracteres inválidos
        ruta_completa = os.path.join(self.carpeta_resultados, nombre_archivo)
        plt.savefig(ruta_completa)
        print(f"✅ Gráfica guardada en: {ruta_completa}")
        plt.close()

    def graficar_valores_nulos(self):
        """Muestra y guarda un gráfico de barras con los valores nulos."""
        nulos_por_columna = self.df.isnull().sum()
        plt.figure(figsize=(10, 5))
        nulos_por_columna.plot(kind='bar', color='red', alpha=0.7)
        plt.title('Valores nulos por columna')
        plt.xlabel('Columnas')
        plt.ylabel('Cantidad de valores nulos')
        self.guardar_grafica("valores_nulos_barras.png")

    def graficar_estadisticas_numericas(self):
        """Genera gráficos de línea para variables numéricas con media, mediana, moda y varianza."""
        df_numerico = self.df.select_dtypes(include=['number'])
        
        if df_numerico.empty:
            print("⚠️ No hay datos numéricos para graficar.")
            return
        
        for columna in df_numerico.columns:
            plt.figure(figsize=(10, 5))
            plt.plot(df_numerico[columna], label="Valores", color="blue")
            plt.axhline(df_numerico[columna].mean(), color="red", linestyle="--", label="Media")
            plt.axhline(df_numerico[columna].median(), color="green", linestyle="--", label="Mediana")
            
            moda = df_numerico[columna].mode().iloc[0] if not df_numerico[columna].mode().empty else None
            if moda:
                plt.axhline(moda, color="purple", linestyle="--", label="Moda")
            
            plt.title(f"Distribución de {columna}")
            plt.legend()
            self.guardar_grafica(f"{columna}_estadisticas.png")

    def graficar_frecuencia_categorias(self):
        """Genera gráficos de pastel para las 5 palabras más repetidas en variables categóricas."""
        df_categorico = self.df.select_dtypes(include=['object'])
        
        for columna in df_categorico.columns:
            top_5 = df_categorico[columna].value_counts().head(5)
            if top_5.empty:
                continue
            
            plt.figure(figsize=(8, 8))
            top_5.plot(kind='pie', autopct='%1.1f%%', colors=sns.color_palette("pastel"))
            plt.title(f"Top 5 valores más repetidos en {columna}")
            self.guardar_grafica(f"{columna}_top5_pastel.png")
  
