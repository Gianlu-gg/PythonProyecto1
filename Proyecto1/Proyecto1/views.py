from django.http import HttpResponse
import datetime
from django.template import loader

def saludo(request):
    return HttpResponse("Hola Django - coder")

def segunda_vista(request):
    return HttpResponse("<br><br>Ya entendimos esto, es muy simple")

def diaDeHoy(request):
    
    dia = datetime.datetime.now()
    
    documentoDeTexto = f"Hoy es dia: <br> {dia}"
    
    return HttpResponse(documentoDeTexto)

def miNombreEs(self, nombre):
    documentoDeTexto = f"Mi nombres es: <br><br>    {nombre}"
    
    return HttpResponse(documentoDeTexto)

def probandoTemplate(self):
    
    nom = "Gianluca"
    ap = "Gonzalez"
    
    listaDeNotas = [2,2,3,7,2,5]
        
    diccionario = {"nombre": nom, "apellido": ap, "diaDeHoy": datetime.datetime.now(), "notas":listaDeNotas}
    
    # # miHtml = open("C:\\Users\\Gonza\\Desktop\\PythonProyecto1\\Proyecto1\\Proyecto1\\plantillas\\template1.html")
    
    # plantilla = Template(miHtml.read())
    
    # miHtml.close()
    
    # miContexto = Context(diccionario)
    
    # documento = plantilla.render(miContexto)
    
    # return HttpResponse(documento)
    
    plantillas = loader.get_template("template1.html")
    
    documento = plantillas.render(diccionario)
    
    return HttpResponse(documento)
