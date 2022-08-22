'''
proyecto python mySql
-abrir asistente
-login o registro
-si elegimos registro creara un usuario en la db
-si elegimos login, identifica al usuario y nos preguntara
-crear nota, mostrar notas, borrarlas
'''
from usuarios import acciones
print("""
Acciones Disponibles:

    -registro
    -login      
          
""")

hazEl=acciones.Acciones()

accion=input("Que deseas hacer: ")

if accion== "registro":
    hazEl.registro()
            
elif accion== "login":
    hazEl.login()
    
   