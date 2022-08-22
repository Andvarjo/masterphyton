print("=======LISTADO PELICULAS======")

peliculas=["batman","spiderman","el senor de los anillos"]

nueva_pelicula= "nada"
while nueva_pelicula != "parar":
    nueva_pelicula=input("Introduce la nueva  pelicula: ")
    if nueva_pelicula!="parar":
        peliculas.append(nueva_pelicula)
    

for pelicula in peliculas:
    print(f"{peliculas.index(pelicula)+1}. {pelicula}")


