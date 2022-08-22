
'''
contador=0

for contador in range(0,5):
    print(f"voy por el elemento {contador+1}")
    
'''
numero_usuario=int(input("de que numero quieres la tabla?: "))
if numero_usuario < 1:
    numero_usuario=1

print(f"tabla de multiplicar del numero : {numero_usuario}")

for numero_tabla  in range(1,11):
    if numero_usuario==20:
        print("este numero no se puede utilizar")
        break   # el break se utiliza para salir del For
    
    print(f"{numero_usuario} x {numero_tabla} = {numero_usuario*numero_tabla}")

else:                          #se puede utilizar el ese para hacer una accion despues de terminar el for
    print("tabla finalizada") 

