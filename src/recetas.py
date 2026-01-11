from collections import defaultdict
from typing import NamedTuple, List, Optional
from datetime import date, datetime
import csv

Ingrediente = NamedTuple("Ingrediente",
                    [("nombre",str),
                     ("cantidad",float),
                     ("unidad",str)])
                         
Receta = NamedTuple("Receta", 
                    [("denominacion", str),
                     ("tipo", str),
                     ("dificultad", str),
                     ("ingredientes", List[Ingrediente]),
                     ("tiempo", int),
                     ("calorias", int),
                     ("fecha", date),
                     ("precio", float)])

#Ejercicio 1
def lee_recetas(filename: str) -> List[Receta]:
    with open(filename, encoding= "utf-8") as f:
        lector = csv.reader(f, delimiter=";")
        next(lector)
        res = []
        for denominacion, tipo, dificultad, ingredientes, tiempo, calorias, fecha, precio in lector:
            ingredientes = parsea_ingredientes(ingredientes)
            tiempo = int(tiempo)
            calorias = int(calorias)
            fecha = datetime.strptime(fecha, "%d/%m/%Y").date()
            precio = parsea_precio(precio)
            tupla = Receta(denominacion, tipo, dificultad, ingredientes, tiempo, calorias, fecha, precio)
            res.append(tupla)
    return res
            
def parsea_ingredientes(ingredientes: str)-> list[Ingrediente]:
    res = []
    partes = ingredientes.split(",")
    for parte in partes:
        parte_limpia = parte.strip()
        if parte_limpia:
            ingredientes_parseados = parseo(parte_limpia)
            res.append(ingredientes_parseados)
    return res

def parseo(ingrediente: list[str])->Ingrediente:
    nombre, cantidad, unidad = ingrediente.split("-")
    return Ingrediente(nombre, float(cantidad), unidad)

def parsea_precio(precio:str)->float:

    precio = float(precio.replace(",","."))
    return precio

#Ejercicio 2
def receta_mas_barata(recetas: List[Receta],tipos: set[str],n: Optional[int] = None) -> Receta:
    filtrado = [r for r in recetas if r.tipo in tipos]
    if not filtrado:
        return None
    
    filtrado.sort(key=lambda t:t.calorias)
    
    if n is not None:
        seleccion = filtrado[:n]
    else:
        seleccion = filtrado
    return min(seleccion, key=lambda t:t.precio)
     
            
            