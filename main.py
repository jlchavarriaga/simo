import requests
from dotenv import load_dotenv
import os
import json

# Carga las variables de entorno desde el archivo .env
load_dotenv()

# Accede a la URL desde la variable de entorno
url = os.getenv('URL')

response = requests.get(url)

if response.status_code == 200:
    print("Data Ok")
else:
    print("Error:", response.status_code)


def extraer_datos(lista_diccionarios):
    """Extrae los datos especificados de una lista de diccionarios.

    Args:
        lista_diccionarios: Una lista de diccionarios con la estructura del ejemplo.

    Returns:
        Una lista de diccionarios con los datos extraídos.
    """

    datos_extraidos = []
    for diccionario in lista_diccionarios:
        # Aquí ya estamos recibiendo un diccionario, no es necesario cargarlo como JSON
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


# Obtener el contenido JSON de la respuesta
data = response.json()  # Cambiado a .json() para obtener directamente una lista de diccionarios

resultados = extraer_datos(data)

# Imprimir los resultados (opcional):
for resultado in resultados:
    print(resultado)
