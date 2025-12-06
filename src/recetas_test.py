from recetas import *
fichero = "data/recetas.csv"
recetas = lee_recetas(fichero)
# for r in recetas:
#     print(r)
    
res = ingredientes_por_unidadre(recetas,"gr")
print(f"Hay {res} ingredientes distintos que se miden en None.")
res1 = ingredientes_por_unidadre(recetas, "gr")
print(f"Hay {res1} ingredientes distintos que se miden en gr.")
res2 = ingredientes_por_unidadre(recetas, "cl")
print(f"Hay {res2} ingredientes distintos que se miden en cl.")


recetas = recetas_con_ingredientes(recetas, {'pimiento', 'tomate', 'cebolla'})
print(recetas)