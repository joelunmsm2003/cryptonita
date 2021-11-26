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
        blank=False, max_length=255,null=True
        
    )
    username = models.CharField(blank=False, max_length=100,null=True,unique=True,)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    confirma_email = models.BooleanField(default=False)
    latitud = models.CharField(blank=False, max_length=100,null=True)
    longitud = models.CharField(blank=False, max_length=100,null=True)
    avatar = models.CharField(blank=False, max_length=1000,null=True)
    name = models.CharField(blank=False, max_length=1000,null=True)
    birthday = models.CharField(blank=False, max_length=1000,null=True)
    address = models.CharField(blank=False, max_length=1000,null=True)
    notes = models.CharField(blank=False, max_length=1000,null=True)

    objects = MyUserManager()

    USERNAME_FIELD = 'username'

    class Meta:
        verbose_name_plural = 'Users'




    def __str__(self):
        return self.username

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


class Job(models.Model):
    user = models.OneToOneField(MyUser, related_name='job', on_delete=models.CASCADE,blank=False,null=True)
    title = models.CharField(blank=False, max_length=1000,null=True)
    company = models.CharField(blank=False, max_length=1000,null=True)

    class Meta:
        ordering = ['title']

    def __str__(self):
        return self.title



class Tag(models.Model):
    user = models.ForeignKey(MyUser, related_name='tags', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    label = models.CharField(blank=False, max_length=1000,null=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name

class Email(models.Model):
    user = models.ForeignKey(MyUser, related_name='emails', on_delete=models.CASCADE, blank=False,null=True)
    email = models.CharField(blank=False, max_length=255,null=True)
    label = models.CharField(blank=False, max_length=1000,null=True)

    class Meta:
        ordering = ['email']

    def __str__(self):
        return self.email

class PhoneNumbers(models.Model):
    user = models.ForeignKey(MyUser, related_name='phoneNumbers', on_delete=models.CASCADE, blank=False,null=True)
    country = models.CharField(blank=False, max_length=1000,null=True)
    number = models.CharField(blank=False, max_length=1000,null=True)
    label = models.CharField(blank=False, max_length=1000,null=True)

    class Meta:
        ordering = ['number']

    def __str__(self):
        return self.number


class Cryptocurrency(models.Model):
    price = models.FloatField(blank=True, max_length=100, null=True)
    symbol =models.CharField(blank=True, max_length=100, null=True)
    icono=models.CharField(blank=True, max_length=100, null=True)
    sigla =models.CharField(blank=True, max_length=100, null=True)
    name =models.CharField(blank=True, max_length=100, null=True)
    trend = models.CharField(blank=True, max_length=100, null=True)
    recommendation = models.CharField(blank=True, max_length=100, null=True)
    activ = models.CharField(blank=True, max_length=100, null=True)
    date = models.DateTimeField(blank=True, null=True,default=datetime.datetime.today())
    user = models.ForeignKey(settings.AUTH_USER_MODEL, blank=True, null=True, on_delete=models.CASCADE)
    market_cap = models.FloatField(blank=True, max_length=100, null=True)
    fully_diluted_market_cap= models.CharField(blank=True, max_length=100, null=True)
    volume_24h= models.CharField(blank=True, max_length=100, null=True)
    volume_24h_market_cap= models.CharField(blank=True, max_length=100, null=True)
    circulating_supply= models.CharField(blank=True, max_length=100, null=True)
    max_supply= models.CharField(blank=True, max_length=100, null=True)
    total_supply= models.CharField(blank=True, max_length=100, null=True)


    class Meta:
        verbose_name_plural = 'Cryptocurrency'

    def __str__(self):
       return self.symbol.upper()+' - '+str(self.price)

compra_venta = (
        ('C', 'Buy'),
        ('V', 'Sell')
    )

class Account(models.Model):
    name = models.CharField(blank=True, max_length=100)
    address = models.CharField(blank=True, max_length=100)
    date = models.DateTimeField(blank=True, null=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, blank=True, null=True, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'Accounts'

    def __str__(self):
       return str(self.name)
       
class Transaction(models.Model):
    quantity = models.FloatField(blank=True, null=True, max_length=100)
    price_per_coin = models.FloatField(blank=True, null=True, max_length=100)
    account = models.ForeignKey(Account, blank=True, null=True, on_delete=models.CASCADE)
    holding = models.FloatField(blank=True, null=True, max_length=100)
    date = models.DateTimeField(blank=True, null=True,default=datetime.datetime.today())
    user = models.ForeignKey(settings.AUTH_USER_MODEL, blank=True, null=True, on_delete=models.CASCADE)
    cryptocurrency = models.ForeignKey(Cryptocurrency, blank=True, null=True, on_delete=models.CASCADE)
    type_transaction = models.CharField(blank=True,max_length=1, choices=compra_venta,null=True)
    status = models.BooleanField(default=False)
    
    class Meta:
        verbose_name_plural = 'Transactions'

    def __str__(self):
       return str(self.cryptocurrency)




    @property
    def ganancia(self):



        if self.cryptocurrency:

            precio=(self.cryptocurrency.price-self.price_per_coin)/self.price_per_coin

            ganancia= precio*self.holding

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
    criptomoneda = models.ForeignKey(Cryptocurrency, blank=True, null=True, on_delete=models.CASCADE)
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







class Portfolio(models.Model):
    cryptocurrency = models.ForeignKey(Cryptocurrency, blank=True, null=True, on_delete=models.CASCADE)
    name = models.FloatField(blank=True, max_length=100, null=True)
    quantity = models.FloatField(blank=True, max_length=100, null=True)
    balance_usd = models.FloatField(blank=True, max_length=100, null=True)
    buy_usd = models.FloatField(blank=True, max_length=100, null=True)
    sell_usd = models.FloatField(blank=True, max_length=100, null=True)
    investing_usd = models.FloatField(blank=True, max_length=100, null=True)
    profit_loss = models.FloatField(blank=True, max_length=100, null=True)
    cambio_hora = models.FloatField(blank=True, max_length=100, null=True)
    cambio_4hora = models.FloatField(blank=True, max_length=100, null=True)
    cambio_dia = models.FloatField(blank=True, max_length=100, null=True)
    date = models.DateTimeField(blank=True, null=True,default=datetime.datetime.today())
    user = models.ForeignKey(settings.AUTH_USER_MODEL, blank=True, null=True, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'Portfolio'

    @property
    def _ganancia_usd_indicador(self):

        crypto=  Cryptocurrency.objects.get(id=self.criptomoneda.id)

        balance_usd=self.cantidad*crypto.precio

        ganancia_usd=balance_usd-self.inversion_usd

        return ganancia_usd