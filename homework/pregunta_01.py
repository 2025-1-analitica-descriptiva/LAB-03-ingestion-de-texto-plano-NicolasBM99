"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta.
"""

# pylint: disable=import-outside-toplevel

import pandas as pd
import re

def pregunta_01():
    """
    Construya y retorne un dataframe de Pandas a partir del archivo
    'files/input/clusters_report.txt'. Los requierimientos son los siguientes:

    - El dataframe tiene la misma estructura que el archivo original.
    - Los nombres de las columnas deben ser en minusculas, reemplazando los
      espacios por guiones bajos.
    - Las palabras clave deben estar separadas por coma y con un solo
      espacio entre palabra y palabra.


    """
    with open("files/input/clusters_report.txt", encoding="utf-8") as file:
        lines = file.readlines()[4:] 

    bloques = []
    bloque = ""
    for line in lines:
        if re.match(r"\s+\d+\s+", line): 
            if bloque:
                bloques.append(bloque)
            bloque = line
        else:
            bloque += line
    bloques.append(bloque)

    data = []
    for bloque in bloques:
        partes = re.split(r"\s{2,}", bloque.strip())
        cluster = int(partes[0])
        cantidad = int(partes[1])
        porcentaje = float(partes[2].replace(",", ".").replace(" %", ""))
        palabras = " ".join(partes[3:]) 
        palabras = re.sub(r"\s+", " ", palabras).strip().replace(".,", ".").replace(" .", ".")
        palabras = palabras.replace(".","")
        data.append([cluster, cantidad, porcentaje, palabras])

    df = pd.DataFrame(data, columns=[
        "cluster",
        "cantidad_de_palabras_clave",
        "porcentaje_de_palabras_clave",
        "principales_palabras_clave"
    ])

    return df

if __name__ == "__main__":
    df = pregunta_01()
    print(df.head())