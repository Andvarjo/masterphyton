#### sacar el porcentaje elejido de un numero que el usuario ingrese

numero=int(input("que numero desea operar?: "))
porcentaje=int(input("que porcentaje dese conocer?: "))


resultado=numero*(porcentaje/100)
print(f"el {porcentaje}% de {numero} es igual a {resultado}")