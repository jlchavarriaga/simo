#data_extractor.py
import time
import requests
import os
from dotenv import load_dotenv
import json

class DataExtractor:
    def __init__(self, base_url):
        """Inicializa la clase con la URL base y carga las variables de entorno."""
        load_dotenv()
        self.base_url = base_url
        if not self.base_url:
            raise ValueError("La URL base no está definida. Verifica el archivo .env.")
        self.data = None

    def fetch_data(self, page=0, convocatoria=None):
        """Realiza la solicitud GET para una página específica y una convocatoria."""
        url = f"{self.base_url}&search_convocatoria={convocatoria}&page={page}"
        response = requests.get(url)
        if response.status_code == 200:
            print(f"Data Ok for page {page}")
            return response.json()
        else:
            print(f"Error {response.status_code} on page {page}")
            return None

    def extraer_datos(self, lista_diccionarios):
        """Extrae los datos especificados de la lista de diccionarios proporcionada.

        Args:
            lista_diccionarios: Una lista de diccionarios con la estructura del ejemplo.

        Returns:
            Una lista de diccionarios con los datos extraídos.
        """
        datos_extraidos = []
        for diccionario in lista_diccionarios:
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

    def fetch_data_init(self):
        """Realiza la solicitud GET y almacena los datos si la respuesta es exitosa."""
        response = requests.get(self.base_url)
        if response.status_code == 200:
            self.data = response.json()
            print("Data Ok")
        else:
            print("Error:", response.status_code)

    def extraer_datos_init(self):
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

    def recorrer_paginas(self, numero_convocatoria, total_paginas, output_file='resultados.json'):
        """Recorre las páginas de la convocatoria y guarda los resultados en un archivo."""
        all_data = []
        for page in range(total_paginas):
            data = self.fetch_data(page=page, convocatoria=numero_convocatoria)
            if data:
                datos_extraidos = self.extraer_datos(data)
                all_data.extend(datos_extraidos)
            time.sleep(2)

        # Guardar todos los datos extraídos en un archivo JSON
        with open(output_file, 'w', encoding='utf-8') as file:
            json.dump(all_data, file, ensure_ascii=False, indent=4)
        print(f"Datos guardados en {output_file}")

    def imprimir_resultados(self, resultados):
        """Imprime los resultados extraídos."""
        for resultado in resultados:
            print(resultado)
