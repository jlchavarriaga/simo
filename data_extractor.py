import requests
import os
from dotenv import load_dotenv

class DataExtractor:
    def __init__(self, url):
        """Inicializa la clase con la URL y carga las variables de entorno."""
        # Carga las variables de entorno desde el archivo .env
        load_dotenv()
        self.url = url
        self.data = None

    def fetch_data(self):
        """Realiza la solicitud GET y almacena los datos si la respuesta es exitosa."""
        response = requests.get(self.url)
        if response.status_code == 200:
            self.data = response.json()
            print("Data Ok")
        else:
            print("Error:", response.status_code)

    def extraer_datos(self):
        """Extrae los datos especificados de la lista de diccionarios almacenada.

        Returns:
            Una lista de diccionarios con los datos extraídos.
        """
        if self.data is None:
            print("No data to extract.")
            return []

        datos_extraidos = []
        for diccionario in self.data:
            nuevo_diccionario = {
                "id": diccionario["id"],
                "convocatoria": diccionario["empleo"]["convocatoria"]["nombre"],
                "nivel": diccionario["empleo"]["gradoNivel"]["nivelNombre"],
                "denominacion": diccionario["empleo"]["denominacion"]["nombre"],
                "salario": diccionario["empleo"]["asignacionSalarial"],
                "descripcion": diccionario["empleo"]["descripcion"],
                "requisitos": diccionario["empleo"]["requisitosMinimos"],
                "vacantes": diccionario["empleo"]["vacantes"][0]["cantidad"],
                "departamento": diccionario["empleo"]["vacantes"][0]["municipio"]["departamento"]["nombre"],
                "municipio": diccionario["empleo"]["vacantes"][0]["municipio"]["nombre"]
            }
            datos_extraidos.append(nuevo_diccionario)

        return datos_extraidos

    def imprimir_resultados(self, resultados):
        """Imprime los resultados extraídos."""
        for resultado in resultados:
            print(resultado)
