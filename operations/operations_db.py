import csv
from typing import List
from models import usuario

ARCHIVO_USUARIOS = 'csv_data/usuario.csv'


# Guardar lista de usuario en CSV
def guardar_peliculas_csv(usuario: List[usuario]):
    with (open(ARCHIVO_USUARIOS, mode='w', newline='') as archivo):
        escritor = csv.writer(archivo)
        escritor.writerow(usuario.__annotations__.keys())
        for usuario in usuario:
            escritor.writerow(usuario.dict().values())
