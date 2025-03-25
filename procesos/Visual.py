import os
import matplotlib.pyplot as plt
import seaborn as sns

class VisualizacionDatos:
    def __init__(self, df):
        self.df = df
        self.carpeta_resultados = "resultados"
        os.makedirs(self.carpeta_resultados, exist_ok=True)

    def guardar_grafica(self, nombre_archivo):
        """Guarda la gráfica en la carpeta 'resultados'."""
        ruta_completa = os.path.join(self.carpeta_resultados, nombre_archivo)
        plt.savefig(ruta_completa)
        print(f"✅ Gráfica guardada en: {ruta_completa}")
        plt.close()

    def graficar_valores_nulos(self):
        """Muestra y guarda un mapa de calor con los valores nulos."""
        plt.figure(figsize=(10, 5))
        sns.heatmap(self.df.isnull(), cmap='viridis', cbar=False)
        plt.title('Mapa de valores nulos')
        self.guardar_grafica("valores_nulos.png")

    def graficar_histogramas(self):
        """Muestra y guarda histogramas para variables numéricas."""
        self.df.hist(figsize=(12, 8), bins=20, edgecolor='black')
        plt.suptitle('Distribución de variables numéricas')
        self.guardar_grafica("histogramas.png")

    def graficar_boxplots(self):
        """Muestra y guarda boxplots de variables numéricas."""
        plt.figure(figsize=(12, 6))
        sns.boxplot(data=self.df)
        plt.xticks(rotation=90)
        plt.title('Boxplot de variables numéricas')
        self.guardar_grafica("boxplots.png")

    def graficar_matriz_correlacion(self):
        """Muestra y guarda la matriz de correlación para variables numéricas."""
        df_numerico = self.df.select_dtypes(include=['number'])
        if df_numerico.empty:
            print("⚠️ No hay datos numéricos para calcular la correlación.")
            return

        plt.figure(figsize=(10, 8))
        matriz_corr = df_numerico.corr().fillna(0)
        sns.heatmap(matriz_corr, annot=True, cmap='coolwarm', fmt=".2f", linewidths=0.5)
        plt.title('Matriz de correlación')
        self.guardar_grafica("matriz_correlacion.png")

    def graficar_valores_categoricos(self):
        """Muestra y guarda gráficos de barras para variables categóricas con menos de 10 categorías únicas."""
        cat_cols = [col for col in self.df.select_dtypes(include=['object']).columns if self.df[col].nunique() < 10]
        if not cat_cols:
            print("No hay variables categóricas con pocas categorías únicas para graficar.")
            return

        fig, axes = plt.subplots(len(cat_cols), 1, figsize=(10, 5 * len(cat_cols)))
        if len(cat_cols) == 1:
            axes = [axes]

        for ax, col in zip(axes, cat_cols):
            sns.countplot(x=self.df[col], ax=ax, palette="viridis")
            ax.set_title(f'Frecuencia de categorías en {col}')
            ax.set_ylabel('Frecuencia')
            ax.set_xticklabels(ax.get_xticklabels(), rotation=45)

        plt.tight_layout()
        self.guardar_grafica("valores_categoricos.png")
  
