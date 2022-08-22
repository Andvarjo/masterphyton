##edad de trabajo entre 18 y 65 años
edadminima=18
edadmaxima=65
edad=int(input("¿cual es tu edad?: "))
####### Operador AND #######
if edad >=18 and edad <=65:
    print("es apto apra trabajar")
else:
    print("no tiene edad para trabajar")

#########operador OR ###########
pais=input("¿de que Pais eres?: ")

if pais== "Mexico" or pais=="España" or pais== "Colombia":
    print(f"{pais}es un pais de habla Hispana\n")
else:
    print(f"{pais} no es un pais de habla Hispana\n")

############ NOT ################

if not pais=="España" or pais=="Alemania":
    print(f"{pais} no está dentro de Europa")
   
else:
    print(f"{pais} está dentro de Europa")
 

'''
operadores logicos

and  Y
or   O
! negacion
not no


'''