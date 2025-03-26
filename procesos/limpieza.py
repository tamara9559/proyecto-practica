import pandas as pd

class Limpieza:
    """
    Clase para realizar tareas de limpieza en un DataFrame de pandas.
    Permite eliminar columnas sensibles y validar tipos de datos.
    """
    
    def __init__(self, df):
        """
        Inicializa la clase con un DataFrame.
        
        :param df: DataFrame de pandas a limpiar.
        """
        self.df = df

    def eliminar_columnas_sensibles(self):
        """
        Elimina columnas con nombres sensibles como 'cedula' o 'direccion'.
        También permite al usuario eliminar otras columnas de forma manual.
        """
        columnas_sensibles = ["cedula", "direccion"]
        self.df = self.df.drop(columns=[col for col in columnas_sensibles if col in self.df.columns], errors="ignore")

        while True:
            print("\nColumnas disponibles:", list(self.df.columns))
            col_a_eliminar = input("Ingrese el nombre de una columna a eliminar (o presione Enter para continuar): ").strip()
            if col_a_eliminar:
                if col_a_eliminar in self.df.columns:
                    self.df = self.df.drop(columns=[col_a_eliminar])
                    print(f"Columna '{col_a_eliminar}' eliminada.")
                else:
                    print("La columna no existe.")
            else:
                break

    def validar_tipo_datos(self):
        """
        Pregunta al usuario si desea verificar el tipo de datos de cada columna
        y reporta si hay valores que no coinciden con el tipo esperado.
        """
        for columna in self.df.columns:
            print(f"\nRevisando columna: {columna}")
            tipo_deseado = input("Ingrese el tipo de dato esperado para esta columna (int, float, str o Enter para omitir): ").strip()

            if tipo_deseado:
                try:
                    tipo_deseado = {"int": int, "float": float, "str": str}[tipo_deseado]
                    
                    # Intentar convertir valores y detectar errores
                    errores = self.df[columna].dropna().apply(lambda x: self.intentar_convertir(x, tipo_deseado))
                    valores_erroneos = errores[errores == False].index.tolist()

                    if valores_erroneos:
                        print(f"⚠️ Valores incorrectos en '{columna}': Filas {valores_erroneos}")
                    else:
                        print(f"✅ Todos los valores en '{columna}' cumplen con el tipo {tipo_deseado.__name__}.")
                except KeyError:
                    print("Tipo de dato no válido. Omitiendo validación.")

    @staticmethod
    def intentar_convertir(valor, tipo):
        """
        Intenta convertir un valor a un tipo específico.
        
        :param valor: Valor a convertir.
        :param tipo: Tipo de dato al que se quiere convertir (int, float, str).
        :return: True si la conversión es exitosa, False si no lo es.
        """
        try:
            tipo(valor)
            return True
        except (ValueError, TypeError):
            return False

    def ejecutar_limpeza(self):
        """
        Ejecuta el proceso de limpieza:
        1. Elimina columnas sensibles.
        2. Valida tipos de datos.
        
        :return: DataFrame limpio.
        """
        self.eliminar_columnas_sensibles()
        self.validar_tipo_datos()
        return self.df