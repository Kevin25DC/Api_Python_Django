#from django.shortcuts import render # esto es para renderizar plantilla
from django.http import JsonResponse
from django.views import View # esta clase se imorrta para las vistas
from .models import autor #,libro,auto_libr
#metodos 
class autorview(View): # esta clase se convertira en una vista, que sea capas de procesar las respuesta
    
    def get(request):
        autores = autor.objects.all()  # Consulta todos los registros del modelo Autor
        if autores.exists():
            datos = {'Mensaje': "Exitoso", 'autores': autores}
        else:
            datos = {'Mensaje': "autores no encontrados"}
        return JsonResponse(datos)

    def post(self,request): 
        pass

    def put(self,request):
        pass

    def delete(self,request):
        pass
    

class libroview(View): # esta clase se convertira en una vista, que sea capas de procesar las respuesta
    
    def get(self,request): 
        libro = libro.objects.all()
        if libro.exits():
            datos ={'Mensaje': "exitoso",'libro':libro}
        else:
            datos ={'Mensaje':"libro encontrado"}
        return JsonResponse(datos)

    def post(self,request):
        pass

    def put(self,request):
        pass

    def delete(self,request):
        pass


class auto_librview(View): # esta clase se convertira en una vista, que sea capas de procesar las respuesta
    
    def get(self,request): 
        auto_librview = auto_librview.objects.all()
        if auto_librview.exits():
            datos ={'Mensaje':"Exitoso",'auto_libr':auto_librview}
        else:
            datos ={'Mensaje':"auto_libr encontrado"}
        return JsonResponse(datos)
    def post(self,request):
        pass

    def put(self,request):
        pass

    def delete(self,request):
        pass
