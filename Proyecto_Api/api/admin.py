from django.contrib import admin
from .models import autor
from .models import libro
from .models import auto_libr

# Register your models here.

admin.site.register(autor)
admin.site.register(libro)
admin.site.register(auto_libr)
