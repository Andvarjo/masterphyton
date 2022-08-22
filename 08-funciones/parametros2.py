#### tablas de multiplicar con funciones

def tabla(x,y):
    print(f"la tabla de multiplicar del numero {x}")
    for contador in range(1,y+1):
        operacion= x *contador
        print(f"{x} x {contador} = {operacion}")
    print("\n")

numero=int(input("intruce la tabla que deseas conocer: "))
numfin=int(input("hasta que tabla quieres conocer?: "))
tabla(numero,numfin)
