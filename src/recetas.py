from typing import NamedTuple, List
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

def lee_recetas(fichero):
    with open(fichero,'rt', encoding="utf-8") as f:
        lector = csv.reader(f, delimiter=";")
        next(lector)
        lista_recetas = []
        for (denominacion, tipo, dificultad, ingredientes, tiempo, calorias, fecha, precio) in lector:
            # Procesamos los datos
            ingredientes = parsea_ingredientes(ingredientes)
            tiempo = int(tiempo)
            calorias = int(calorias)
            fecha = datetime.strptime(fecha, "%d/%m/%Y").date()
            precio = float(precio.replace(',', '.'))
            
            # Creamos la tupla
            recetas = Receta(denominacion, tipo, dificultad, ingredientes, tiempo, calorias, fecha, precio)
            lista_recetas.append(recetas)
    return lista_recetas
            
            
def parsea_ingredientes(ingrediente_str: str) -> List[Ingrediente]:
    lista_ingredientes = []
    
    # Separamos por comas
    partes = ingrediente_str.split(",")
    
    for parte in partes:
        # 1. Quitamos espacios sobrantes alrededor (strip)
        parte_limpia = parte.strip()
        
        # 2. IMPORTANTE: Solo procesamos si la cadena NO está vacía
        if parte_limpia: 
            ingrediente_parseado = parsea_ingrediente(parte_limpia)
            lista_ingredientes.append(ingrediente_parseado)
            
    return lista_ingredientes
    

def parsea_ingrediente(ingrediente_str: str) -> Ingrediente:
    # Aquí llega la cadena ya limpia, por ejemplo "Tomate-2-ud"
    nombre, cantidad, unidad = ingrediente_str.split("-")
    return Ingrediente(nombre, float(cantidad),unidad)

def ingredientes_por_unidadre(recetas: list[Receta], unidad: str | None = None )-> int:
    lista = []
    for e in recetas:
        for i in e.ingredientes:
            if unidad == None or i.unidad == unidad:
                lista.append(i.nombre)
    return len(set(lista))

def recetas_con_ingredientes(recetas: list[Receta],conjunto : {str,str})-> list[tuple[str,int,float]]:
    lista = []
    lista_sin_repetidos = []
    for e in recetas:
        for i in e.ingredientes:
            if i.nombre in conjunto:
                lista.append((e.denominacion, e.calorias,e.precio))
    for orden in lista:
        if orden not in lista_sin_repetidos:
            lista_sin_repetidos.append(orden)
        
    return lista_sin_repetidos

def receta_mas_barata(recetas: list[Receta], conjunto : {str,str}, n : int| None == None)-> list[Receta]:
            lista = []
            n == None
            for e in recetas:
                
                