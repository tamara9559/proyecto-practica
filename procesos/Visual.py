import matplotlib.pyplot as plt
import seaborn as sns

class VisualizacionDatos:
    def __init__(self, df):
        self.df = df

    def graficar_valores_nulos(self):
        """Muestra un mapa de calor con los valores nulos del DataFrame."""
        plt.figure(figsize=(10, 5))
        sns.heatmap(self.df.isnull(), cmap='viridis', cbar=False)
        plt.title('Mapa de valores nulos')
        plt.show()

    def graficar_histogramas(self):
        """Muestra histogramas para todas las variables numéricas."""
        self.df.hist(figsize=(12, 8), bins=20, edgecolor='black')
        plt.suptitle('Distribución de variables numéricas')
        plt.show()

    def graficar_boxplots(self):
        """Muestra boxplots para detectar valores atípicos en variables numéricas."""
        plt.figure(figsize=(12, 6))
        sns.boxplot(data=self.df)
        plt.xticks(rotation=90)
        plt.title('Boxplot de variables numéricas')
        plt.show()

    def graficar_matriz_correlacion(self):
        """Muestra un heatmap con la matriz de correlación entre variables numéricas."""
        plt.figure(figsize=(10, 8))
        matriz_corr = self.df.corr().fillna(0)  # Reemplazar NaN con 0
        sns.heatmap(matriz_corr, annot=True, cmap='coolwarm', fmt=".2f", linewidths=0.5)
        plt.title('Matriz de correlación')
        plt.show()


    def graficar_valores_categoricos(self):
        """Muestra gráficos de barras para variables categóricas con menos de 10 categorías únicas."""
        cat_cols = [col for col in self.df.select_dtypes(include=['object']).columns if self.df[col].nunique() < 10]
        if not cat_cols:
            print("No hay variables categóricas con pocas categorías únicas para graficar.")
            return
        
        fig, axes = plt.subplots(len(cat_cols), 1, figsize=(10, 5 * len(cat_cols)))
        if len(cat_cols) == 1:
            axes = [axes]  # Ajustar si hay solo una gráfica

        for ax, col in zip(axes, cat_cols):
            sns.countplot(x=self.df[col], ax=ax, palette="viridis")
            ax.set_title(f'Frecuencia de categorías en {col}')
            ax.set_ylabel('Frecuencia')
            ax.set_xticklabels(ax.get_xticklabels(), rotation=45)

        plt.tight_layout()
        plt.show()
