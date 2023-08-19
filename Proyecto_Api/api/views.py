#from django.shortcuts import render # esto es para renderizar plantilla
from django.http import JsonResponse
from django.views import View # esta clase se imorrta para las vistas
from .models import autor,libro,auto_libr
#metodos 
class autorview(View): # esta clase se convertira en una vista, que sea capas de procesar las respuesta
        def get(self, request):
            autores = autor.objects.all()
            autores_serializados = list(autores.values())  # Convertir el QuerySet en una lista de diccionarios
            if autores_serializados:
                 datos = {'Mensaje': "Exitoso", 'autores': autores_serializados}
            else:
                datos = {'Mensaje': "autores no encontrados"}
            return JsonResponse(datos)

   

class libroview(View): # esta clase se convertira en una vista, que sea capas de procesar las respuesta
    
    def get(self,request): 
        libros = libro.objects.all()
        libro_serializados = list(libros.values()) 
        if libro_serializados:
            datos ={'Mensaje': "exitoso",'libro':libro_serializados}
        else:
            datos ={'Mensaje':"libro encontrado"}
        return JsonResponse(datos)

    

class auto_librview(View): # esta clase se convertira en una vista, que sea capas de procesar las respuesta

    
    def get(self,request): 
        autos_librview = auto_libr.objects.all()
        autos_libr_serializados =list(autos_librview.values())
        if autos_libr_serializados:
            datos ={'Mensaje':"Exitoso",'auto_libr':autos_libr_serializados}
        else:
            datos ={'Mensaje':"auto_libr encontrado"}
        return JsonResponse(datos)
