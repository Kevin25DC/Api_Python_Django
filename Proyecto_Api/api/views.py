#from django.shortcuts import render # esto es para renderizar plantilla
from typing import Any
from django import http
from django.http import JsonResponse
from django.views import View # esta clase se imorrta para las vistas
from .models import autor,libro,auto_libr
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
#metodos 
class autorview(View): # esta clase se convertira en una vista, que sea capas de procesar las respuesta
        
        @method_decorator (csrf_exempt)
        def dispatch(self, request, *args: Any, **kwargs):  #este metodo es para hacer una peticion, el cual coloque para que no hubiera problema al momento de insertar un datos en la bse de datos desde un Json
            return super().dispatch(request, *args, **kwargs)
        
        def get(self, request):
            autores = autor.objects.all()
            autores_serializados = list(autores.values())  # Convertir el QuerySet en una lista de diccionarios
            if autores_serializados:
                 datos = {'Mensaje': "Exitoso", 'autores': autores_serializados}
            else:
                datos = {'Mensaje': "autores no encontrados"}
            return JsonResponse(datos)
        
        def post(self, request):
            try:
        # Aquí realizas la inserción de datos en la base de datos
        # Por ejemplo, si 'nombre' y 'apellido' son campos de tu modelo 'autor':
                nombre = request.POST.get('nombre')
                apellido = request.POST.get('apellido')
                ciudad = request.POST.get('ciudad')
                fecha_creacion = request.POST.get('fecha_creacion')
                nuevo_autor = autor(nombre=nombre, apellido=apellido, ciudad=ciudad,fecha_creacion=fecha_creacion)
                nuevo_autor.save()

                datos = {'Mensaje': "Datos insertados exitosamente"}
            except Exception as e:
                datos = {'Mensaje': "Error al insertar datos"}
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
