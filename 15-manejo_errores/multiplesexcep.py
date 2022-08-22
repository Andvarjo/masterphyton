
try:
    numero=int(input("numero para elevar al cuadrado: "))
    print("el cuadrado de el numero es: " +str(numero*numero))

except TypeError:
    print("debes convertir tus cadenas a enteros")

except ValueError:
    print("debes introducir un numero")
#except Exception as error:
 #   print(type(error))
  #  print("ha ocurrido un error ", type(error).__name__)
