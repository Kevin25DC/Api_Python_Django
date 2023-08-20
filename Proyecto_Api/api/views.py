#from django.shortcuts import render # esto es para renderizar plantilla
from typing import Any
from django import http
from django.http import JsonResponse
from django.views import View # esta clase se imorrta para las vistas
from .models import autor,libro,auto_libr
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
import json 
#metodos 
class autorview(View): # esta clase se convertira en una vista, que sea capas de procesar las respuesta
        
        @method_decorator (csrf_exempt)
        def dispatch(self, request, *args: Any, **kwargs):  #este metodo es para hacer una peticion, el cual coloque para que no hubiera problema al momento de insertar un datos en la bse de datos desde un Json
            return super().dispatch(request, *args, **kwargs)
        
        def get(self, request, id=0):
            if id > 0:
                autores_lista = list(autor.objects.filter(id=id).values())
                if len(autores_lista) > 0:
                    autor_info = autores_lista[0]
                    datos = {'Mensaje': "Exitoso", 'autores': autor_info}
                else:
                    datos = {'Mensaje': "autores no encontrados"}
                return JsonResponse(datos)
            else:
                autores_lista = list(autor.objects.values())
                if len(autores_lista) > 0:
                    datos = {'Mensaje': "Exitoso", 'autores': autores_lista}
                else:
                    datos = {'Mensaje': "autores no encontrados"}
            return JsonResponse(datos)



        
        def post(self, request):
            # print(request.body)
            jd=json.loads(request.body)
            #print(jd)
            autor.objects.create(nombre=jd['nombre'], apellido =jd ['apellido'], ciudad =jd['ciudad'], fecha_creacion =jd ['fecha_creacion'])
            datos = {'Mensaje':"Exitoso"}
            return JsonResponse(datos)
        
        def put(self,request):
            jd=json.loads(request.body)
            autor = list(autor.objects.filter(id=id).values())
            if len(autor) > 0:
                autor = autor.objects.get(id=id)
                autor.nombre =jd['nombre_autor']
                autor.apellido =jd['apellido']
                autor.ciduad =jd['ciduad']
                autor.fecha =jd['fecha_de_creacion']
                autor.save()
            else:
                datos ={'Mnesaje':"libro no encontrado"}

class libroview(View): # esta clase se convertira en una vista, que sea capas de procesar las respuesta
    
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args: Any, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self,request): 
        libros = libro.objects.all()
        libro_serializados = list(libros.values()) 
        if libro_serializados:
            datos ={'Mensaje': "exitoso",'libro':libro_serializados}
        else:
            datos ={'Mensaje':"libro encontrado"}
        return JsonResponse(datos)
    
    def post(self,request):
        jd =json.loads(request.body)
        libro.objects.create(nombre_libro =jd['nombre_libro'], tema =jd['tema'],fecha =jd ['tema'])
        datos ={'Mensaje':"libro insertado exitosamente"}
        return JsonResponse(datos)
    

class auto_librview(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args: Any, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request): 
        autos_librview = auto_libr.objects.all()
        autos_libr_serializados = list(autos_librview.values())
        if autos_libr_serializados:
            datos = {'Mensaje': "Exitoso", 'auto_libr': autos_libr_serializados}
        else:
            datos = {'Mensaje': "auto_libr no encontrado"}
        return JsonResponse(datos)
    
    def post(self, request):
        try:
            data = json.loads(request.body)
            autor_id = data['autor_id']  # Supongamos que el JSON incluye el ID del autor
            libro_id = data['libro_id']  # Supongamos que el JSON incluye el ID del libro
           
           
            autor_relacionado = autor.objects.get(id2_autor=autor_id)  # Obtén el autor relacionado
            libro_relacionado = libro.objects.get(id1_dlibro=libro_id)  # Obtén el libro relacionado
            
            nueva_relacion = auto_libr(
                autor=autor_relacionado,
                libro=libro_relacionado,
                fecha=data['fecha_auto_libr']
            )
            nueva_relacion.save()
            print(nueva_relacion)
             

            response_data = {'Mensaje': "auto_libr insertado exitosamente"}
        except Exception as e:
            print(e)
            response_data = {'Mensaje': "Error al insertar auto_libr"}
        
        return JsonResponse(response_data)
