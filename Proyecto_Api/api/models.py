from django.db import models

# Create your models here.

class autor(models.Model):
    nombre =models.CharField(max_length =100,blank=False)
    apellido =models.CharField(max_length=100, blank=False)
    ciudad= models.CharField (max_length=100,blank=False)
    fecha_creacion=models.CharField(max_length=100)
def __str__(self):
	    return ('(' + str(self.nombre) + ') '+self.apellido + self.ciudad + self.fehca_creacion)

class libro(models.Model):
    nombre_libro =models.CharField(max_length=100, blank=False)
    tema =models.CharField(max_length=100, blank=False)
    fecha =models.CharField(max_length=100)
def __str__(self):
       return(self.nombre_libro + self.tema + self.fecha)

class auto_libr(models.Model):
       id1_dlibro = models.ForeignKey(libro,on_delete=models.CASCADE)
       id2_autor = models.ForeignKey(autor,on_delete=models.CASCADE)
       fecha_auto_libr =models.CharField(max_length=100)
def __str__(self):
       return(self.id1_dlibro + self.id2.id2_autor + self.fecha_auto_libr)