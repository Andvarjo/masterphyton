import mysql.connector

database=mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="master_python"
             
)


# la conexion es correcta?

#print(database)


#cursor que eprmite hacer consultas

cursor=database.cursor(buffered=True)
#crear base de datos
'''

cursor.execute("CREATE DATABASE IF NOT EXISTS master_python")

cursor.execute("SHOW DATABASES")

for bd in cursor:
    print(bd)

#crear tablas
'''

cursor.execute("""
CREATE TABLE IF NOT EXISTS vehiculos(
id int(10) auto_increment not null,
marca varchar(40) not null,
modelo varchar(40) not null,
precio float(10,2) not null, 
CONSTRAINT pk_vehiculo PRIMARY KEY(id)   
)               
"""   
)
#insertar valores

#cursor.execute("INSERT INTO vehiculos VALUES(null,'Opel','Astra',18500)")
#database.commit()

coches=[
    ('Seat','ibiza',5000),
    ('Mazda','cx5',15000),
    ('Fiat','mobi',4000),
    ('Suzuki','Swift',5000)  
]

#cursor.executemany("INSERT INTO vehiculos VALUES(null,%s,%s,%s)",coches)
#LIstar registros
cursor.execute("SELECT * FROM vehiculos") # si reemplazo el * con el nombre de la columna me saca los datos asociados ej marca
result=cursor.fetchall()

print("todos mis coches: ")
for coche in result:
    print(coche[1],coche[3]) # puedo acceder a marca y precio

print("-----coches precio menor a 5000----")
cursor.execute("SELECT * FROM vehiculos WHERE precio <=5000")
result=cursor.fetchall()
for coche in result:
    print(coche[1],coche[2],coche[3])
    
    
print("-----coches FIAT precio menor a 5000----")
cursor.execute("SELECT * FROM vehiculos WHERE precio <=5000 AND marca = 'Fiat'") 
result=cursor.fetchall()
for coche in result:
    print(coche[1],coche[2],coche[3])
    
# sacar un solo dato
cursor.execute("SELECT * FROM vehiculos ")
coche= cursor.fetchone() # se usa fetch one
print(coche)

# eliminar un registro
cursor.execute("DELETE FROM vehiculos WHERE marca = 'Mazda'")
print(cursor.rowcount, "borrados!!") #puedo saber cuantos elementos borrados

#actualizar datos

cursor.execute("UPDATE vehiculos SET modelo='Vitara' WHERE marca='Suzuki'")