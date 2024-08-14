import json

def filtrar_y_ordenar_por_palabra_clave(input_file, output_file, palabra_clave):
    """
    Filtra los datos de un archivo JSON según una palabra clave en los requisitos y los ordena por número de vacantes.

    Args:
        input_file: El archivo JSON de entrada.
        output_file: El archivo JSON donde se guardarán los resultados filtrados y ordenados.
        palabra_clave: La palabra clave a buscar en los estudios de los requisitos.
    """
    with open(input_file, 'r', encoding='utf-8') as file:
        datos = json.load(file)

    # Filtrar los datos que contienen la palabra clave en los estudios de los requisitos
    datos_filtrados = []
    for item in datos:
        requisitos = item.get("requisitos", [])
        for req in requisitos:
            estudio = req.get("estudio", "")
            if palabra_clave.lower() in estudio.lower():
                datos_filtrados.append(item)
                break

    # Ordenar los datos filtrados por número de vacantes de mayor a menor
    datos_ordenados = sorted(datos_filtrados, key=lambda x: x["vacantes"], reverse=True)

    # Guardar los resultados en el archivo de salida
    with open(output_file, 'w', encoding='utf-8') as file:
        json.dump(datos_ordenados, file, ensure_ascii=False, indent=4)

    print(f"Datos filtrados y ordenados guardados en {output_file}")

