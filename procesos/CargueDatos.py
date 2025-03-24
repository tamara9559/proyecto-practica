from pathlib import Path##sgregada 
import pandas as pd

class CargueDatos:
    def __init__(self, datos=None):
        """
        Inicializa la clase con la carpeta de datos opcional.
        Si no se proporciona, se pedirá al usuario seleccionar un archivo.
        """
        self.carpeta_datos = Path(datos) if datos else None

    def listar_archivos(self, extension=[".xlsx", ".csv"]):
       """
       Lista los archivos con las extensiones especificadas en la carpeta de datos.
       """
       if self.carpeta_datos and self.carpeta_datos.exists():
        return [archivo for archivo in self.carpeta_datos.iterdir() if archivo.suffix in extension]
       return []


    def cargar_datos(self, archivo=None):
        """
        Carga un archivo de datos. Si no se proporciona, permite la selección manual.
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
