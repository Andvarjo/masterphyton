'''''

def saludame(nombre):
    saludo=f"hola, saludos {nombre}"
    
    return saludo

print(saludame("andres varela"))

'''

'''generar calculadora en un string'''

numero1=input("cual es el primer numero?")
numero2=input("cual es el segundo numero?")
operaciones= input("operaciones basicas?")
def calculadora(numero1,numero2,basicas= True):
    suma= numero1+numero2
    resta= numero1-numero2
    multi= numero1*numero2
    division=numero1/numero2
    
    cadena=""
    if basicas!= False:
        cadena+="suma: " +str(suma)
        cadena+="\n"
        cadena+="resta: " +str(resta)
        cadena+="\n"
    else:
        cadena+="multipliacion: " +str(multi)
        cadena+="\n"
        cadena+="division: " +str(division)
    
    return cadena

print(calculadora(5,5))
    
    
    