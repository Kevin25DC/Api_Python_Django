from django.contrib import admin
from .models import autores
from .models import revista
from .models import articulo
from .models import autores_articulos

# Register your models here.

admin.site.register(autores)
admin.site.register(revista)
admin.site.register(articulo)
admin.site.register(autores_articulos)