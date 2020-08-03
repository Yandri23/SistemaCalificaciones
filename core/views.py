from django.shortcuts import render, HttpResponse

# Create your views here.
html_base = """
    <h1>Mi Menu</h1>
    <ul>
        <li>   <a href="/">Inicio</a>              </li>
        <li>   <a href="/alumnos/">Alumnos</a>   </li>
        <li>   <a href="/profesores/">Profesores</a>   </li>
        <li>   <a href="/calificaciones/">Calificaciones</a>   </li>
        <li>   <a href="/secretaria/">Secretaria</a>   </li>
        <li>   <a href="/about-me/">Acerca de</a>   </li>
        <li>   <a href="/contact/">Contacto</a>     </li>
        <li>   <a href="/portfolio/">porfolio</a>     </li>
    </ul>
"""



def home(request):
    html_response = "<h1>la pagina de Portadas</h1>"
    html_response = html_base + html_response
    return HttpResponse(html_response);

def contact(request):
    html_response = "<h1>la pagina de Contacto</h1>"
    html_response = html_base + html_response
    return HttpResponse(html_response);

def about(request):
    html_response = "<h1>la pagina de Acerca de</h1>"
    html_response = html_base + html_response
    return HttpResponse(html_response);

def alumnos(request):
    html_response = "<h1>la pagina de Alumnos</h1>"
    html_response = html_base + html_response
    return HttpResponse(html_response);

def profesores(request):
    html_response = "<h1>la pagina de Profesores</h1>"
    html_response = html_base + html_response
    return HttpResponse(html_response);

def calificaciones(request):
    html_response = "<h1>la pagina de Calificaciones</h1>"
    html_response = html_base + html_response
    return HttpResponse(html_response);

def secretaria(request):
    html_response = "<h1>la pagina de Secretaria</h1>"
    html_response = html_base + html_response
    return HttpResponse(html_response);


# Template tag
# block content
# extends
# url

def home(request, plantilla="home.html"):
    return render(request, plantilla)

def about(request, plantilla="about.html"):
    return render(request, plantilla)

def contact(request, plantilla="contact.html"):
    return render(request, plantilla)

def alumnos(request, plantilla="alumnos.html"):
    return render(request, plantilla)

def profesores(request, plantilla="profesores.html"):
    return render(request, plantilla)

def calificaciones(request, plantilla="calificaciones.html"):
    return render(request, plantilla)

def secretaria(request, plantilla="secretaria.html"):
    return render(request, plantilla)

def portfolio(request, plantilla="portfolio.html"):
    return render(request, plantilla)