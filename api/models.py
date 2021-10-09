from django.db import models
import datetime
from django.contrib.auth.models import AbstractUser
from django.conf import settings
import requests
from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)



class MyUserManager(BaseUserManager):
    def create_user(self, username,date_of_birth, password=None):

        if not username:
            raise ValueError('Users must have an username')

        user = self.model(
            username=username,
        )

        user.set_password(password)
        user.is_admin=True
        user.save(using=self._db)
        return user

    def create_superuser(self, username=None, email=None, password=None):
        user = self.create_user(
            username = username,
            password=password,
            date_of_birth="2020-01-01"
        )
        return user


class MyUser(AbstractBaseUser):
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        
    )
    username = models.CharField(blank=False, max_length=100,null=True,unique=True,)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    confirma_email = models.BooleanField(default=False)
    latitud = models.CharField(blank=False, max_length=100,null=True)
    longitud = models.CharField(blank=False, max_length=100,null=True)

    objects = MyUserManager()

    USERNAME_FIELD = 'username'

    class Meta:
        verbose_name_plural = 'Usuarios'




    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin



class Criptomonedas(models.Model):
    precio = models.FloatField(blank=True, max_length=100, null=True)
    simbolo =models.CharField(blank=True, max_length=100, null=True)
    icono=models.CharField(blank=True, max_length=100, null=True)
    sigla =models.CharField(blank=True, max_length=100, null=True)
    nombre =models.CharField(blank=True, max_length=100, null=True)
    tendencia = models.CharField(blank=True, max_length=100, null=True)
    recomendacion = models.CharField(blank=True, max_length=100, null=True)
    activo = models.CharField(blank=True, max_length=100, null=True)
    fecha = models.DateTimeField(blank=True, null=True,default=datetime.datetime.today())
    user = models.ForeignKey(settings.AUTH_USER_MODEL, blank=True, null=True, on_delete=models.CASCADE)
    market_cap = models.FloatField(blank=True, max_length=100, null=True)
    fully_diluted_market_cap= models.CharField(blank=True, max_length=100, null=True)
    volume_24h= models.CharField(blank=True, max_length=100, null=True)
    volume_24h_market_cap= models.CharField(blank=True, max_length=100, null=True)
    circulating_supply= models.CharField(blank=True, max_length=100, null=True)
    max_supply= models.CharField(blank=True, max_length=100, null=True)
    total_supply= models.CharField(blank=True, max_length=100, null=True)




    class Meta:
        verbose_name_plural = 'Criptomonedas'

    def __str__(self):
       return self.simbolo.upper()+' - '+str(self.precio)

compra_venta = (
        ('C', 'Compra'),
        ('V', 'Venta')
    )

class Cuentas(models.Model):
    nombre = models.CharField(blank=False, max_length=100)
    address = models.CharField(blank=False, max_length=100)
    fecha = models.DateTimeField(blank=True, null=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, blank=True, null=True, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'Cuentas'

    def __str__(self):
       return str(self.nombre)
       
class Inversion(models.Model):
    cantidad_comprada = models.FloatField(blank=True, null=True, max_length=100)
    cuenta = models.ForeignKey(Cuentas, blank=True, null=True, on_delete=models.CASCADE)
    precio_usd = models.FloatField(blank=True, null=True, max_length=100)
    comprada_usd = models.FloatField(blank=True, null=True, max_length=100)
    fecha = models.DateTimeField(blank=True, null=True,default=datetime.datetime.today())
    user = models.ForeignKey(settings.AUTH_USER_MODEL, blank=True, null=True, on_delete=models.CASCADE)
    criptomoneda = models.ForeignKey(Criptomonedas, blank=True, null=True, on_delete=models.CASCADE)
    transaccion = models.CharField(blank=True,max_length=1, choices=compra_venta,null=True)
    eliminado = models.BooleanField(default=False)
    
    class Meta:
        verbose_name_plural = 'Inversiones'

    def __str__(self):
       return str(self.criptomoneda)




    @property
    def ganancia(self):

        '''

        url='https://blockchain.info/tobtc?currency=USD&value=1000'

        response=requests.get(url)

        cantidad=float(response.text)

        self.criptomoneda.precio=1000/cantidad

        '''

        if self.criptomoneda:

            precio=(self.criptomoneda.precio-self.precio_usd)/self.precio_usd

            ganancia= precio*self.comprada_usd

            return ganancia

        else:

            return 0




    @property
    def porcentaje_ganancia(self):

        if self.criptomoneda:

            precio=(self.criptomoneda.precio-self.precio_usd)/self.precio_usd

            ganancia= precio*100
            
            return ganancia

        else:

            return 0



class Historial(models.Model):
    criptomoneda = models.ForeignKey(Criptomonedas, blank=True, null=True, on_delete=models.CASCADE)
    open_price = models.FloatField(blank=True, max_length=100, null=True)
    close_price = models.FloatField(blank=True, max_length=100, null=True)
    high_price = models.FloatField(blank=True, max_length=100, null=True)
    low_price = models.FloatField(blank=True, max_length=100, null=True)
    price = models.FloatField(blank=True, max_length=100, null=True)
    fecha = models.DateTimeField(blank=True, null=True)
    creator = models.ForeignKey(settings.AUTH_USER_MODEL, blank=True, null=True, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'Historial'

    def __str__(self):
       return str(self.price)







class Portofolio(models.Model):
    criptomoneda = models.ForeignKey(Criptomonedas, blank=True, null=True, on_delete=models.CASCADE)
    cantidad = models.FloatField(blank=True, max_length=100, null=True)
    balance_usd = models.FloatField(blank=True, max_length=100, null=True)
    comprada_usd = models.FloatField(blank=True, max_length=100, null=True)
    venta_usd = models.FloatField(blank=True, max_length=100, null=True)
    inversion_usd = models.FloatField(blank=True, max_length=100, null=True)
    ganancia_usd = models.FloatField(blank=True, max_length=100, null=True)
    cambio_hora = models.FloatField(blank=True, max_length=100, null=True)
    cambio_4hora = models.FloatField(blank=True, max_length=100, null=True)
    cambio_dia = models.FloatField(blank=True, max_length=100, null=True)
    fecha = models.DateTimeField(blank=True, null=True,default=datetime.datetime.today())
    user = models.ForeignKey(settings.AUTH_USER_MODEL, blank=True, null=True, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'Portafolio'

    @property
    def _ganancia_usd_indicador(self):

        crypto=  Criptomonedas.objects.get(id=self.criptomoneda.id)

        balance_usd=self.cantidad*crypto.precio

        ganancia_usd=balance_usd-self.inversion_usd

        return ganancia_usd