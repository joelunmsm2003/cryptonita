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


class InversionsSerializer(serializers.ModelSerializer):
	class Meta:
		model =  Inversion 
		fields = "__all__"

