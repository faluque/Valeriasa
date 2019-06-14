from django.db import models, connections
from django.contrib.auth.models import AbstractUser

class usuarios(AbstractUser):
    administrativo= 'A'
    cliente='I'
    tipo_opciones=(
        (administrativo, 'Administrador'),
        (cliente,'Inquilino'),
        )
    password=models.BinaryField()
    passtxt=models.CharField(max_length=45)
    tipoUsr=models.CharField(max_length=15,
                             choices=tipo_opciones,
                             default=administrativo,)
    nro_inquilino=models.IntegerField(null=True,blank=True, unique=True)

    def check_password(self, password):
       cur = connections['default'].cursor()
       res=cur.callproc("sp_login", [self.username, password, 0,0])
       cur.close()
       if res[0]!='F' and res[1]!='-1':
           return True
    
    
    
       

class ctacte(models.Model):
    nro_inquilino=models.IntegerField(null=True,blank=True, unique=True)
    detalle=models.CharField(max_length=200)
    importe=models.CharField(max_length=15)
    fecha= models.DateField(auto_now_add=True)  
    concepto= models.CharField(max_length=10)
    saldo= models.CharField(max_length=15, blank=True)
    factura=models.CharField(max_length=15, blank=True)
    sociedad= models.CharField(max_length=10, blank=True)



