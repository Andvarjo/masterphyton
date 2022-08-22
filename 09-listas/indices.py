peliculas=["batman","spiderman","el senor de los anillos"]
cantantes=list(('2pac','drake','future')) #convierte una tupla en lista
year=list(range(2020,2050))
variada=["andres",1,4.4,True]

pelicula_nueva="otracosa"
#indices 
print(peliculas[1])
print(peliculas[-2])
print(cantantes[0:2]) #saca solo los datos dentro del rango

print(peliculas[1:]) # saca todos los elemntos de la lista apartir del indice 1

peliculas[1]=pelicula_nueva #puedo modificar datos direccionados

print(peliculas)