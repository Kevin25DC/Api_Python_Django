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
        
        def put(self, request, id):
            jd = json.loads(request.body)
            autores_lista = list(autor.objects.filter(id=id).values())
            if len(autores_lista) > 0:
                autor_obj = autor.objects.get(id=id)  
                autor_obj.nombre = jd['nombre']
                autor_obj.apellido = jd['apellido']
                autor_obj.ciduad = jd['ciudad']
                autor_obj.fecha = jd['fecha_creacion']
                autor_obj.save()
                datos = {'Mensaje': "Exitoso"}
            else:
                datos = {'Mensaje': "libro no encontrado"}
            return JsonResponse(datos)

        def delete(self, request, id):
            try:
                autor_obj = autor.objects.get(id=id)
                autor_obj.delete()
                datos = {'Mensaje': "Autor eliminado exitosamente"}
                return JsonResponse(datos)
            except autor.DoesNotExist:
                datos = {'Mensaje': "Autor no encontrado"}
                return JsonResponse(datos)
