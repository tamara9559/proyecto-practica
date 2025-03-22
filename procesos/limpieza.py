import pandas as pd

class LimpiezaDatos:
    def __init__(self, df):
        """
        Inicializa la clase con un DataFrame de pandas.
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
                    valores_erroneos = self.df[columna].dropna().apply(lambda x: not isinstance(x, tipo_deseado))

                    if valores_erroneos.any():
                        print(f"⚠️ Hay {valores_erroneos.sum()} valores en '{columna}' que no son {tipo_deseado.__name__}.")
                    else:
                        print(f"✅ Todos los valores en '{columna}' cumplen con el tipo {tipo_deseado.__name__}.")
                except KeyError:
                    print("Tipo de dato no válido. Omitiendo validación.")

    def ejecutar_limpeza(self):
        """
        Ejecuta el proceso de limpieza: elimina columnas sensibles y valida tipos de datos.
        """
        self.eliminar_columnas_sensibles()
        self.validar_tipo_datos()
        return self.df
