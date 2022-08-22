

nombre=input("cual es tu nombre?: ")
edad=int(input("que edad tienes?: "))
def mostrartunombre(x, y):
    print(f"tu nombre es: {x}")
    if y>=18:
        print(f"eres mayoor de edad y tienes {y} años")
    else:
        print(f"eres menor de edad y tienes {y} años")
mostrartunombre(nombre,edad)