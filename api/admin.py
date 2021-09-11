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



@admin.register(Criptomonedas)
class CriptomonedasAdmin(admin.ModelAdmin):
    list_display = ('id','nombre','simbolo','precio','sigla','activo','tendencia')
    list_filter = ('precio',)
    search_fields=('nombre','sigla')
    #list_editable = ('activo',)



@admin.register(Historial)
class HistorialAdmin(admin.ModelAdmin):
    list_display = ('id','price','criptomoneda','fecha',)
    list_filter = ('criptomoneda',)

@admin.register(Cuentas)
class CuentasAdmin(admin.ModelAdmin):
    list_display = ('id','nombre',)


@admin.register(Portofolio)
class PortofolioAdmin(admin.ModelAdmin):
    list_display = ('id','criptomoneda','cantidad','_balance_usd','comprada_usd','venta_usd','inversion_usd','_ganancia_usd','porcentaje')

    def _balance_usd(self, obj):

        crypto=  Criptomonedas.objects.get(id=obj.criptomoneda.id)

        balance_usd=round(obj.cantidad*crypto.precio,3)

        return balance_usd

    def porcentaje(self, obj):

        _historial=Historial.objects.filter(criptomoneda_id=obj.criptomoneda.id).order_by('-id')[:6000]

        try:

            ultimo_hora=(_historial[0].price-_historial[60].price)*100/float(_historial[20].price)

            ultimo_4hora=(_historial[0].price-_historial[60*4].price)*100/float(_historial[80].price)

            ultimodia=(_historial[0].price-_historial[6*24].price)*100/float(_historial[20*24].price)

        except:

            ultimo_hora=0
            ultimo_4hora=0
            ultimodia=0

        crypto=  Criptomonedas.objects.get(id=obj.criptomoneda.id)

        crypto.nombre=crypto.nombre.replace('-','_')


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

        return format_html('<a style="color:red;" target="_blank" href="http://app01.comunica7.com:5500/monedas/'+crypto.nombre+'/NaN/Binance" >'+str(texto)+'</a>')
 

    def _ganancia_usd(self, obj):

        crypto=  Criptomonedas.objects.get(id=obj.criptomoneda.id)

        balance_usd=obj.cantidad*crypto.precio

        ganancia_usd=balance_usd-obj.inversion_usd

        if int(ganancia_usd)<0:
            return format_html('<span  style="color:red;">'+str(round(ganancia_usd,3))+'</span>')
        else:
            return format_html('<span  style="color:green;">'+str(round(ganancia_usd,3))+'</span>')


'''
@admin.register(HistorialUser)
class HistorialUserAdmin(admin.ModelAdmin):
    list_display = ('id','price','criptomoneda','fecha','ganancia')
    list_filter = ('criptomoneda',)

'''

@admin.register(Inversion)
class InversionsAdmin(admin.ModelAdmin):
    list_display = ('id','criptomoneda','cantidad_comprada','comprada_usd','_ganancia','transaccion','fecha')
    list_filter = ('criptomoneda','transaccion')
   
    actions = ['actualizar']

    def save_model(self, request, obj, form, change):

        super(InversionsAdmin, self).save_model(request, obj, form, change)

        inv=Inversion.objects.get(id=obj.id)
        inv.comprada_usd=round(obj.cantidad_comprada*obj.precio_usd,3)
        inv.save()

        _inversion=Inversion.objects.filter(criptomoneda_id=obj.criptomoneda.id,eliminado=False).order_by('id')

        crypto=  Criptomonedas.objects.get(id=obj.criptomoneda.id)

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

            print(i.transaccion)

            if i.transaccion=='C':
                signo=1
            else:
                signo=-1


            if signo==1:
                cantidad_comprada=cantidad_comprada+i.cantidad_comprada*signo
                comprada_usd=comprada_usd+i.comprada_usd
            else:
                cantidad_vendida=cantidad_vendida+i.cantidad_comprada*signo
                vendida_usd=vendida_usd+i.comprada_usd

        print(cantidad_comprada,cantidad_vendida)

        cantidad=round(cantidad_comprada+cantidad_vendida,3)

        balance_usd=cantidad*crypto.precio

        inversion_usd=comprada_usd-vendida_usd

        ganancia_usd=balance_usd-inversion_usd

        Portofolio(criptomoneda_id=obj.criptomoneda.id,cantidad=cantidad,balance_usd=round(balance_usd,3),comprada_usd=round(comprada_usd,3),venta_usd=round(vendida_usd,3),inversion_usd=round(inversion_usd,3),ganancia_usd=round(ganancia_usd,3)).save()



    def _comprada_usd(self, obj):
        return obj.comprada_usd

    def _ganancia(self, obj):
        return round(obj.ganancia,2)


    def _porcentaje_ganancia(self, obj):
        return round(obj.porcentaje_ganancia,2)


    def actualizar(self, request,queryset):

        url='http://app01.comunica7.com:5500/seteaprecio'

        response=requests.get(url)

        print(response.text)

        return 'Ok'

