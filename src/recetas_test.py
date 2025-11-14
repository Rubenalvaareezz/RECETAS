from recetas import *
fichero = "data/recetas.csv"
recetas = lee_recetas(fichero)
for r in recetas:
    print(r)


