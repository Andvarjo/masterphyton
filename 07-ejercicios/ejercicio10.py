'''
el programa tiene que pedir la nota de x alumnos y sacar en pantalla cuantos
han aprobado y cuantos han reprobado

'''

numest=int(input("ingrese el numero de estudiantes: "))
contador=1
aprobado=0
reprobado=0

while contador<=numest:
    calificacion=float(input(f"ingrese calificacion del estudiante nro {contador} :"))
    if calificacion>5 or calificacion<0:
     print("nota invalida")
    else:
      if calificacion>=3:
        aprobado+=1
      else:
        reprobado+=1
      contador+=1
print(f"han aprobado {aprobado} estudiantes y reprobado {reprobado} estudiantes")

    