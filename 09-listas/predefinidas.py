cantantes=["2pac","drake","bad bunny","kanye"]
numeros=[1,2,5,8,3,4]

# ordenar una lista

print(numeros)
numeros.sort()
print(numeros)\

#anadir elementos

cantantes.append("lil wayne")
cantantes.insert(1,"ice cube")
print(cantantes)  

#eliminar elementos

cantantes.pop(1) #elimina el de la posicion 1
cantantes.remove("drake") #eliminar un dato en concreto
print(cantantes)

#dar la vuelta
print(numeros)
numeros.reverse()
print(numeros)

#buscar dentro de lista

print("lil wayne"in cantantes)

#contar elementos
print(len(cantantes))

#cuantas veces aparece un elemento 

cantantes.append("lil wayne")
print(cantantes.count("lil wayne"))

#conseguir indice

print(cantantes.index("2pac"))

#unir listas

cantantes.extend(numeros)
print(cantantes)