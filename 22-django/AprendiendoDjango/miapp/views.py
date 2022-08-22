from django.shortcuts import render,HttpResponse, redirect

# Create your views here.

#MVC = modelo vista controlador
#MVT = modelo template vista -> el template es la vista y el vista es el controlador


layout= """
<h1> Sitio web con Django ~ Andres varela </h1>
<hr/>
<ul>
    <li>
        <a href="/inicio"> INICIO </a>
    </li>
    
    <li>
        <a href="/hola-mundo"> Hola Mundo </a>
    </li>
    
    <li>
        <a href="/pagina-pruebas"> Pagina de pruebas </a>
    </li>
    
    <li>
        <a href="/contacto"> contacto </a>
    </li>
</ul>
<hr/>

"""


def index(request):
    
    html= """
    <h1> INICIO </h1>                    
    <p> Odd years before 2050: </p>
    <ul>                    
    """
    year = 2021
    while year <= 2050:
        if year %2 == 0:
            html += f"<li>{str(year)}</li>"
        year += 1
    
    html += "</ul>"
    return render(request,'index.html')

def holaMundo(request):
    return render(request,'hola_mundo.html')

def pagina(request,redirigir=0):
    
    if redirigir == 1:
            return redirect('contacto',nombre = "Andres", apellidos = "Varela")
    
    return render(request,'pagina.html')
    
def contacto(request,nombre = "",apellidos = ""):
    
    html = ""
    
    if nombre and apellidos:
        html = "<p>El nombre completo es:</p>"
        html += f"<h3> {nombre} {apellidos} </h3>"
    
    return HttpResponse(layout + f"<h2> Pagina de contacto <h2/>"+html)