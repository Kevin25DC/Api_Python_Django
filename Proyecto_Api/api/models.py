from django.db import models

# Create your models here.

class autores(models.Model):
    id_autor = models.CharField(max_length=500, verbose_name='campo id autor', unique=True)
    nombre_autor = models.CharField(max_length=500,verbose_name='nombre del autor',blank=False)
    afiliacion_autor =models.CharField(max_length=500, verbose_name='nombre de la afiliacion A', blank=False)
    
    def __str__(self):
	    return ('(' + str(self.id_autor) + ') '+self.nombre_autor + self.afiliacion_autor)
    

class revista(models.Model):
    id_revista = models.CharField(max_length=500, verbose_name='campo id autor', unique=True)
    nombre_revista = models.CharField(max_length=500,verbose_name='nombre de la revista ',blank=False)
    issn1 =models.CharField(max_length=500, verbose_name='cedula revista #1', blank=False)
    issn2 =models.CharField(max_length=500, verbose_name='cedula revista #2', blank=False)
    issn3 =models.CharField(max_length=500, verbose_name='cedula revista #3', blank=False)
    issn4 =models.CharField(max_length=500, verbose_name='cedula revista #4', blank=False)
    cuartil =models.CharField (max_length=500, verbose_name='cedula revista #4', blank=False)
    ciudad=models.CharField(max_length=500, verbose_name='ciudad', blank=False)
    region=models.CharField(max_length=500, verbose_name='region', blank=False)
    publicador=models.CharField(max_length=500, verbose_name='publicador', blank=False)
    
    def __str__(self):
	    return ('(' + str(self.id_revista) + ') '+self.nombre_revista + self.issn1 + self.issn2
             +self.issn3 + self.issn4 + self.cuartil + self.ciudad + self.region + self.publicador)
    

class articulo(models.Model):
    id_articulo = models.CharField(max_length=500, verbose_name='campo id autor', unique=True)
    titulo_del_articulo = models.CharField(max_length=500,verbose_name='titulo del articulo',blank=False)
    fecsys =models.DateTimeField(max_length=500, verbose_name='fecha del articulo', auto_now_add=True)
    id_revista_articulo =models.ForeignKey(revista, on_delete=models.CASCADE)

    def __str__(self):
	    return ('(' + str(self.id_articulo) + ') '+self.titulo_del_articulo + self.fecsys + self.id_revista_articulo)

class autores_articulos(models.Model):
    id_autor_articulo =models.CharField(max_length=500, verbose_name='id autor del articulo',unique=True)
    id_autor_A = models.ForeignKey(autores, on_delete=models.CASCADE) 
    id_articulo_A = models.ForeignKey(articulo, on_delete=models.CASCADE) 

    def __str__(self):
          return (+str(self.id_autor_A + self.id_articulo_A + self.id_autor_articulo))
    

#class revista_cuartil(models.Model):
#    id_revista_Q =models.ForeignKey(revista, max_length=500, verbose_name='id autor del articulo',unique=True)
#    id_autor_A = models.ForeignKey(autores, on_delete=models.CASCADE) 
#    id_articulo_A = models.ForeignKey(articulo, on_delete=models.CASCADE) 

#   def __str__(self):
#         return (+str(self.id_autor_A + self.id_articulo_A + self.id_autor_articulo))

