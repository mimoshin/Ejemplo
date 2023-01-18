from django.db import models

# Create your models here.
class modeloprueba(models.Model):
    nombre= models.CharField(max_length=200, default='default')
    edad = models.IntegerField(default=10)
    nacimiento = models.DateField(auto_now=True)

    def __str__(self) -> str:
        #funcion de descripcion base del objeto
        return f"{self.nombre} - {self.edad} - {self.nacimiento}"


"""
REVISAR DECLARACION DE MODELOS

 class nombre_modelo(models.Model):
    ...atributo 1...
    ...atributo 2...
    ...atributo 3...

"""