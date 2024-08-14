from data_extractor import DataExtractor
import os

if __name__ == "__main__":
    url = os.getenv('URL')
    extractor = DataExtractor(url)
    extractor.fetch_data()
    resultados = extractor.extraer_datos()
    extractor.imprimir_resultados(resultados)
