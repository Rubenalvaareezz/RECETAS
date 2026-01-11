from recetas import *
fichero = "data/recetas.csv"
recetas = lee_recetas(fichero)
for r in recetas[:2]:
    print(r)
print("------------")
ejercicio2 = receta_mas_barata(recetas,tipos={"Postre", "Entrante"},n=None)
print(ejercicio2)