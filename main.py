# main.py
from data_extractor import DataExtractor
import os
from dotenv import load_dotenv

load_dotenv()

def demo():
    url = os.getenv('URL')
    if not url:
        raise ValueError("La URL no está definida. Verifica el archivo .env.")
    extractor = DataExtractor(url)
    extractor.fetch_data()
    resultados = extractor.extraer_datos()
    extractor.imprimir_resultados(resultados)


def save_data():
    base_url = os.getenv('URL_BASE')
    if not base_url:
        raise ValueError("La URL base no está definida. Verifica el archivo .env.")
    extractor = DataExtractor(base_url)

    # Parámetros para la búsqueda
    numero_convocatoria = "826070830"  # Ejemplo, actualízalo según tus necesidades
    total_paginas = 2  # Ejemplo, actualízalo según tus necesidades

    # Recorrer las páginas y guardar los resultados en un archivo
    extractor.recorrer_paginas(numero_convocatoria, total_paginas, output_file='resultados.json')

if __name__ == "__main__":
    save_data()
