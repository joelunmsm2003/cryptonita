from rest_framework import serializers
from .models import *
import logging
from rest_framework.decorators import authentication_classes, permission_classes

@permission_classes([])
class CriptomonedasSerializer(serializers.ModelSerializer):
	class Meta:
		model = Criptomonedas 
		fields = "__all__"

@permission_classes([])
class HistorialSerializer(serializers.ModelSerializer):
	class Meta:
		model = Historial 
		fields = "__all__"

@permission_classes([])
class HistorialUserSerializer(serializers.ModelSerializer):
	class Meta:
		model = HistorialUser 
		fields = "__all__"

class InversionsSerializer(serializers.ModelSerializer):
	class Meta:
		model =  Inversion 
		fields = "__all__"

class MovieSerializer(serializers.ModelSerializer):
	class Meta:
		model = Movie 
		fields = "__all__"

class MedidasSerializer(serializers.ModelSerializer):
	class Meta:
		model = Medidas 
		fields = "__all__"


class SubcategoriaSerializer(serializers.ModelSerializer):
	class Meta:
		model = Subcategoria 
		fields = "__all__"


class CategoriaSerializer(serializers.ModelSerializer):
	class Meta:
		model = Categoria 
		fields = "__all__"


class FavoritosSerializer(serializers.ModelSerializer):
	class Meta:
		model = Favoritos 
		fields = "__all__"


class CercademiSerializer(serializers.ModelSerializer):
	local = serializers.StringRelatedField(many=False)
	user = serializers.StringRelatedField(many=False)

	class Meta:
		model = Cercademi 
		fields = ['local','user','foto_local','descripcion']


class PromocionSerializer(serializers.ModelSerializer):
	local = serializers.StringRelatedField(many=False)
	user = serializers.StringRelatedField(many=False)

	class Meta:
		model = Promocion 
		fields = ['local','user','foto_local']

