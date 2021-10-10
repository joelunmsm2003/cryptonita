from django import forms
from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.core.exceptions import ValidationError
import requests
from .models import *
from django.utils.html import format_html




class UserAdmin(BaseUserAdmin):
    # The forms to add and change user instances
    
    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    list_display = ('username', 'is_admin','confirma_email')
    list_filter = ('is_admin',)
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal informacion', {'fields': ('username',)}),
        ('Permissions', {'fields': ('is_admin',)}),
    )
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'password1', 'password2'),
        }),
    )
    search_fields = ('email',)
    ordering = ('email',)
    filter_horizontal = ()


# Now register the new UserAdmin...
admin.site.register(MyUser, UserAdmin)
# ... and, since we're not using Django's built-in permissions,
# unregister the Group model from admin.
admin.site.unregister(Group)



@admin.register(Cryptocurrency)
class CryptocurrencyAdmin(admin.ModelAdmin):
    list_display = ('crypto','symbol','name','price','market_cap','volume_24h','circulating_supply')
    search_fields=('nombre','sigla')
    #list_editable = ('activo',)

    def crypto(self, obj):

        if obj.icono:
            return format_html('<img style="max-width:25px;" src="'+obj.icono+'" ></img>')
        else:
            return obj.nombre


@admin.register(Historial)
class HistorialAdmin(admin.ModelAdmin):
    list_display = ('id','price','criptomoneda','fecha',)
    list_filter = ('criptomoneda',)

@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    list_display = ('id','name',)


@admin.register(Portfolio)
class PortfolioAdmin(admin.ModelAdmin):
    list_display = ('crypto','cryptocurrency','quantity','_balance_usd','buy_usd','sell_usd','investing_usd','_profit_loss')

    def crypto(self, obj):

        crypto=  Cryptocurrency.objects.get(id=obj.cryptocurrency.id)

        return format_html('<img style="max-width:25px;" src="'+crypto.icono+'" ></img>')

    def _balance_usd(self, obj):

        crypto=  Cryptocurrency.objects.get(id=obj.cryptocurrency.id)

        balance_usd=round(obj.quantity*crypto.price,3)

        return balance_usd

    def percentaje(self, obj):

        _historial=Historial.objects.filter(criptomoneda_id=obj.cryptocurrency.id).order_by('-id')[:6000]

        try:

            ultimo_hora=(_historial[0].price-_historial[60].price)*100/float(_historial[20].price)

            ultimo_4hora=(_historial[0].price-_historial[60*4].price)*100/float(_historial[80].price)

            ultimodia=(_historial[0].price-_historial[6*24].price)*100/float(_historial[20*24].price)

        except:

            ultimo_hora=0
            ultimo_4hora=0
            ultimodia=0

        crypto=  Cryptocurrency.objects.get(id=obj.cryptocurrency.id)

        crypto.nombre=crypto.name.replace('-','_')


        if ultimodia<0:

            ultimodia ="<span style='color:red;'>"+str(round(ultimodia,2))+"</span>"

        else:

            ultimodia ="<span style='color:green;'>"+str(round(ultimodia,2))+"</span>"

        if ultimo_4hora<0:

            ultimo_4hora ="<span style='color:red;'>"+str(round(ultimo_4hora,2))+"</span>"

        else:

            ultimo_4hora ="<span style='color:green;'>"+str(round(ultimo_4hora,2))+"</span>"

        if ultimo_hora<0:

            ultimo_hora ="<span style='color:red;'>"+str(round(ultimo_hora,2))+"</span>"

        else:

            ultimo_hora ="<span style='color:green;'>"+str(round(ultimo_hora,2))+"</span>"
            
        texto="<span style='display:grid;grid-template-columns:auto auto auto;'>"+"<span>"+ultimodia+"</span><span>"+ultimo_4hora+"</span><span>"+ultimo_hora+"</span></span>"

        url='http://localhost:5500/admin/api/inversion/?criptomoneda__id__exact='+str(crypto.id)

        return format_html('<a style="color:red;" target="_blank" href="'+url+'" >'+str(texto)+'</a>')
 
    def _profit_loss(self, obj):

        crypto=  Cryptocurrency.objects.get(id=obj.cryptocurrency.id)

        url='http://localhost:5500/admin/api/transaction/?cryptocurrency__id__exact='+str(crypto.id)

        return format_html('<a style="color:red;" target="_blank" href="'+url+'" >'+str(obj.profit_loss)+'</a>')

    def recomendacion(self, obj):

        crypto=  Cryptocurrency.objects.get(id=obj.criptomoneda.id)

        if crypto.recomendacion=='BUY' or crypto.recomendacion=='STRONG_BUY':

            return format_html('<a style="color:green;" >'+str(crypto.recomendacion)+'</a>')

        if crypto.recomendacion=='SELL' or crypto.recomendacion=='STRONG_SELL':

            return format_html('<a style="color:RED;" >'+str(crypto.recomendacion)+'</a>')

        return crypto.recomendacion


    def _ganancia_usd(self, obj):

        crypto=  Cryptocurrency.objects.get(id=obj.criptomoneda.id)

        balance_usd=obj.cantidad*crypto.price

        ganancia_usd=balance_usd-obj.inversion_usd

        if ganancia_usd<0:
            return format_html('<span  style="color:red;">'+str(round(ganancia_usd,3))+'</span>')
        else:
            return format_html('<span  style="color:green;">'+str(round(ganancia_usd,3))+'</span>')




@admin.register(Transaction)
class TransactionsAdmin(admin.ModelAdmin):
    list_display = ('id','cryptocurrency','account','quantity','holding','profit_loss','type_transaction','date')
    list_filter = ('account','cryptocurrency','type_transaction')
   
    actions = ['actualizar']

    def save_model(self, request, obj, form, change):

        super(TransactionsAdmin, self).save_model(request, obj, form, change)

        inv=Transaction.objects.get(id=obj.id)
        inv.holding=round(obj.quantity*obj.price_per_coin,3)
        inv.save()

        _inversion=Transaction.objects.filter(cryptocurrency_id=obj.cryptocurrency.id,status=False).order_by('id')

        crypto=  Cryptocurrency.objects.get(id=obj.cryptocurrency.id)

        _in=0

        ganancia_inversion=0
        ganancia_total=0
        cantidad_comprada=0
        cantidad_vendida=0
        comprada_usd=0
        vendida_usd=0
        balance=0

        for i in _inversion:

            elem_gan=[]
            _in=_in+1
            elem_gan.insert(1,_in)

            print(i.type_transaction)

            if i.type_transaction=='C':
                signo=1
            else:
                signo=-1


            if signo==1:
                cantidad_comprada=cantidad_comprada+i.quantity*signo
                comprada_usd=comprada_usd+i.holding
            else:
                cantidad_vendida=cantidad_vendida+i.quantity*signo
                vendida_usd=vendida_usd+i.holding

        print(cantidad_comprada,cantidad_vendida)

        cantidad=round(cantidad_comprada+cantidad_vendida,3)

        balance_usd=cantidad*crypto.price

        inversion_usd=comprada_usd-vendida_usd

        ganancia_usd=balance_usd-inversion_usd

        Portfolio.objects.filter(cryptocurrency_id=obj.cryptocurrency.id).delete()

        Portfolio(cryptocurrency_id=obj.cryptocurrency.id,quantity=cantidad,balance_usd=round(balance_usd,3),buy_usd=round(comprada_usd,3),sell_usd=round(vendida_usd,3),investing_usd=round(inversion_usd,3),profit_loss=round(ganancia_usd,3)).save()



    def holding(self, obj):
        return obj.holding

    def profit_loss(self, obj):

        if obj.ganancia<0:
            return format_html('<span  style="color:red;">'+str(round(obj.ganancia,3))+'</span>')
        else:
            return format_html('<span  style="color:green;">'+str(round(obj.ganancia,3))+'</span>')




    def _porcentaje_ganancia(self, obj):
        return round(obj.porcentaje_ganancia,2)


    def actualizar(self, request,queryset):

        url='http://app01.comunica7.com:5500/seteaprecio'

        response=requests.get(url)

        print(response.text)

        return 'Ok'

