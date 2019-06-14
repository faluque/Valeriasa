from django.db import models
from django.contrib.auth.models import AbstractUser

class usuarios(AbstractUser):
    administrativo= 'A'
    cliente='I'
    tipo_opciones=(
        (administrativo, 'Administrador'),
        (cliente,'Inquilino'),
        )
    passtxt=models.CharField(max_length=45)
    tipoUsr=models.CharField(max_length=15,
                             choices=tipo_opciones,
                             default=administrativo,)
    
       

class ctacte(models.Model):
    inquilino=models.ForeignKey(usuarios)
    detalle=models.CharField(max_length=200)
    importe=models.CharField(max_length=15)
    fecha= models.DateField(auto_now_add=True)  
    concepto= models.CharField(max_length=10)
    saldo= models.CharField(max_length=15, blank=True)
    factura=models.CharField(max_length=15, blank=True)
    sociedad= models.CharField(max_length=10, blank=True)



