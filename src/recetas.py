from typing import NamedTuple,List
from datetime import date,datetime
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


def lee_recetas(fichero):
    with open (fichero, encoding = "utf-8") as f:
        lector = csv.reader(f)
        next(lector)
        recetas= []
        for denominacion,tipo,dificultad,ingredientes,tiempo,calorias,fecha,precio in lector:
            
            ingredientes = parsea_ingrediente(ingredientes) 
            tiempo = int(tiempo)
            calorias = int(calorias)
            fecha = datetime.strptime(fecha, "%d/%m/%Y").date()
            precio = float(precio)
            receta= Receta(denominacion,tipo,dificultad,ingredientes,tiempo,calorias,fecha,precio)
            recetas.append(receta)
    return recetas

def parsea_ingredientes(ingredientes_str: str) -> List[Ingrediente]:
    lista=[]
 
    for ingrediente in ingredientes_str.split(","):
        lista.append(parsea_ingredientes(ingredientes_str))
    return lista


def parsea_ingrediente(ingredientes_str:str) ->Ingrediente:
    nombre, cantidad, unidad = ingredientes_str.split("-")
    return Ingrediente(nombre, float(cantidad), unidad)