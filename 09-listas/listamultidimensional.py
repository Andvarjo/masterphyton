
print("\n**********listado de contactos******")

contactos=[
    [
        'Andres',
        'andres@andres.com'
    ],
    [
        'felipe',
        'felipe@felipe.com'
    ],
    [
        'Varela',
        'Varela@varela.com'
    ]
           
]

#print(contactos[0][1])

for contacto in contactos:
    for elemento in contacto:
        if contacto.index(elemento)==0:
            print("nombre : "+ elemento)
        else:
            print("correo : " + elemento)
    print("\n")