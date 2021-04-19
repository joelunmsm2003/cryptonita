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
    precio = models.FloatField(blank=False, max_length=100, null=True)
    simbolo =models.CharField(blank=False, max_length=100, null=True)
    icono=models.CharField(blank=False, max_length=100, null=True)
    sigla =models.CharField(blank=False, max_length=100, null=True)
    nombre =models.CharField(blank=False, max_length=100, null=True)
    tendencia = models.CharField(blank=False, max_length=100, null=True)
    activo = models.CharField(blank=True, max_length=100, null=True)
    fecha = models.DateTimeField(blank=True, null=True,default=datetime.datetime.today())
    user = models.ForeignKey(settings.AUTH_USER_MODEL, blank=True, null=True, on_delete=models.CASCADE)

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



class HistorialUser(models.Model):
    criptomoneda = models.ForeignKey(Criptomonedas, blank=True, null=True, on_delete=models.CASCADE)
    ganancia = models.FloatField(blank=True, max_length=100, null=True)
    price = models.FloatField(blank=True, max_length=100, null=True)
    fecha = models.DateTimeField(blank=True, null=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, blank=True, null=True, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'HistorialUser'

    def __str__(self):
       return str(self.price)





class Movie(models.Model):
    title = models.CharField(blank=False, max_length=100)
    released = models.IntegerField(blank=False)
    genre = models.CharField(blank=False, max_length=100)
    creator = models.ForeignKey(settings.AUTH_USER_MODEL, blank=True, null=True, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'Movies'

    def __str__(self):
       return self.title

class Medidas(models.Model):
    menu = models.CharField(blank=False, max_length=100)
    medida =models.CharField(blank=False, max_length=100)
    label = models.CharField(blank=False, max_length=100)
    fecha = models.DateTimeField(blank=True, null=True,default=datetime.datetime.today())
    user = models.ForeignKey(settings.AUTH_USER_MODEL, blank=True, null=True, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'Medidas'

    def __str__(self):
       return self.menu



class Categoria(models.Model):
    nombre = models.CharField(blank=False, max_length=100)
    foto = models.FileField(upload_to='static',blank=True, null=True)
    fecha = models.DateTimeField(blank=True, null=True,default=datetime.datetime.today())
    descripcion = models.CharField(blank=False, max_length=1000,null=True)


    class Meta:
        verbose_name_plural = 'Categorias'

    def __str__(self):
       return self.nombre

class Subcategoria(models.Model):
    nombre = models.CharField(blank=False, max_length=100)
    foto = models.FileField(upload_to='static',blank=True, null=True)
    categoria = models.ForeignKey(Categoria, blank=True, null=True, on_delete=models.CASCADE)
    fecha = models.DateTimeField(blank=True, null=True,default=datetime.datetime.today())
    descripcion = models.CharField( max_length=1000,blank=False, null=True)

    class Meta:
        verbose_name_plural = 'Subcateogorias'

    def __str__(self):
       return self.nombre

class Local(models.Model):
    nombre = models.CharField(blank=False, max_length=100)
    foto = models.FileField(upload_to='static',blank=True, null=True)
    subcategoria = models.ForeignKey(Subcategoria, blank=True, null=True, on_delete=models.CASCADE)
    fecha = models.DateTimeField(blank=True, null=True,default=datetime.datetime.today())
    descripcion = models.CharField( max_length=1000,blank=False, null=True)

    class Meta:
        verbose_name_plural = 'Locales'

    def __str__(self):
       return self.nombre

class Promocion(models.Model):
    nombre = models.CharField(blank=False, max_length=100)
    local = models.ForeignKey(Local, blank=True, null=True, on_delete=models.CASCADE)
    fecha = models.DateTimeField(blank=True, null=True,default=datetime.datetime.today())
    descuento = models.CharField(blank=False, max_length=100)

    class Meta:
        verbose_name_plural = 'Promocion'

    def __str__(self):
       return self.nombre

    @property
    def foto_local(self):

        #foto=Local.objects.get(id=self.id).foto
        return str(self.local.foto)


class Favoritos(models.Model):
    local = models.ForeignKey(Local, blank=True, null=True, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, blank=True, null=True, on_delete=models.CASCADE)
    fecha = models.DateTimeField(blank=True, null=True,default=datetime.datetime.today())

    class Meta:
        verbose_name_plural = 'Favoritos'

    def __str__(self):
       return self.local.nombre

class Cercademi(models.Model):
    local = models.ForeignKey(Local, blank=True, null=True, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, blank=True, null=True, on_delete=models.CASCADE)
    fecha = models.DateTimeField(blank=True, null=True,default=datetime.datetime.today())


    class Meta:
        verbose_name_plural = 'Cerca de mi'


    @property
    def foto_local(self):

        #foto=Local.objects.get(id=self.id).foto
        return str(self.local.foto)

    @property
    def descripcion(self):

        #foto=Local.objects.get(id=self.id).foto
        return str(self.local.descripcion)


