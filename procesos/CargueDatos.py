from pathlib import Path  # Importa la clase Path para manejar rutas de archivos
import pandas as pd  # Importa pandas para manipulación de datos

class CargueDatos:
    """
    Clase para gestionar la carga de archivos de datos desde una carpeta específica.
    Permite listar archivos disponibles y cargarlos en un DataFrame de pandas.
    """
    def __init__(self, datos=None):
        """
        Inicializa la clase con la carpeta de datos opcional.
        Si no se proporciona, se pedirá al usuario seleccionar un archivo manualmente.

        :param datos: Ruta de la carpeta donde se encuentran los archivos de datos (opcional).
        """
        self.carpeta_datos = Path(datos) if datos else None

    def listar_archivos(self, extension=[".xlsx", ".csv"]):
        """
        Lista los archivos disponibles en la carpeta de datos con las extensiones especificadas.

        :param extension: Lista de extensiones de archivo a buscar (por defecto, .xlsx y .csv).
        :return: Lista de archivos encontrados con las extensiones dadas.
        """
        if self.carpeta_datos and self.carpeta_datos.exists():
            return [archivo for archivo in self.carpeta_datos.iterdir() if archivo.suffix in extension]
        return []

    def cargar_datos(self, archivo=None):
        """
        Carga un archivo de datos en un DataFrame de pandas.
        Si no se proporciona un archivo, solicita al usuario la ruta manualmente.

        :param archivo: Ruta del archivo a cargar (opcional).
        :return: DataFrame de pandas con los datos cargados o None si hay un error.
        """
        if archivo:
            ruta_archivo = Path(archivo)
        else:
            ruta_archivo = Path(input("Ingrese la ruta del archivo de datos: ").strip())

        if ruta_archivo.exists() and ruta_archivo.suffix in [".csv", ".xlsx"]:
            if ruta_archivo.suffix == ".csv":
                return pd.read_csv(ruta_archivo)
            else:
                return pd.read_excel(ruta_archivo)
        else:
            print("El archivo no existe o no tiene un formato válido (.csv, .xlsx).")
            return None
