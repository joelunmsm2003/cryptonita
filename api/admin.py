from django import forms
from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.core.exceptions import ValidationError
import requests
from .models import *





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
    list_display = ('id','nombre','simbolo','precio','sigla','activo')
    list_filter = ('precio',)
    search_fields=('nombre','sigla')
    list_editable = ('activo',)



@admin.register(Historial)
class HistorialAdmin(admin.ModelAdmin):
    list_display = ('id','price','criptomoneda','fecha',)
    list_filter = ('criptomoneda',)


@admin.register(HistorialUser)
class HistorialUserAdmin(admin.ModelAdmin):
    list_display = ('id','price','criptomoneda','fecha','ganancia')
    list_filter = ('criptomoneda',)



@admin.register(Inversion)
class InversionsAdmin(admin.ModelAdmin):
    list_display = ('id','criptomoneda','_comprada_usd','precio_usd','cantidad_comprada','_ganancia','_porcentaje_ganancia','transaccion','fecha')
    list_filter = ('criptomoneda','transaccion')

    actions = ['actualizar']

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

