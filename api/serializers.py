from rest_framework import serializers
from .models import *
import logging
from rest_framework.decorators import authentication_classes, permission_classes

@permission_classes([])
class CryptocurrencySerializer(serializers.ModelSerializer):
	class Meta:
		model = Cryptocurrency 
		fields = "__all__"

@permission_classes([])
class HistorialSerializer(serializers.ModelSerializer):
	class Meta:
		model = Historial 
		fields = "__all__"


class TransactionsSerializer(serializers.ModelSerializer):
	class Meta:
		model =  Transaction 
		fields = "__all__"

