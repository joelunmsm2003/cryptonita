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

@permission_classes([])
class GenericSerializer(serializers.ModelSerializer):
	class Meta:
		model = Generic 
		fields = "__all__"


class TransactionsSerializer(serializers.ModelSerializer):
	class Meta:
		model =  Transaction 
		fields = "__all__"

class AccountsSerializer(serializers.ModelSerializer):
	class Meta:
		model =  Account 
		fields = "__all__"

class EmailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Email
        fields = "__all__"


class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = "__all__"


class PhoneNumbersSerializer(serializers.ModelSerializer):
    class Meta:
        model = PhoneNumbers
        fields = "__all__"

class TagRelatedField(serializers.RelatedField):
    def display_value(self, instance):
        return instance

    def to_representation(self, value):
        return str(value)

    def to_internal_value(self, data):
        return Tag.objects.filter(name=data)[0]


class MyUserSerializer(serializers.ModelSerializer):

	emails = EmailSerializer(many=True)
	phoneNumbers = PhoneNumbersSerializer(many=True)
	job = JobSerializer(many=False)
	tags = TagRelatedField(
        queryset=Tag.objects.all(),
        many=True
    )

	class Meta:
		model =  MyUser 
		fields = "__all__"

	def update(self, instance, validated_data):


		phoneNumbers=validated_data.get('phoneNumbers')

		obj=MyUser.objects.filter(username=instance)
		

		PhoneNumbers.objects.filter(user__username=instance).delete()
		
		for p in phoneNumbers:

			p['user_id']=obj[0].id

			PhoneNumbers(**p).save()


		validated_data.pop('emails')
		validated_data.pop('job')
		validated_data.pop('tags')
		validated_data.pop('phoneNumbers')



		obj.update(**validated_data)

		instance=MyUser.objects.get(username=instance)


		return instance



	def __init__(self, *args, **kwargs):
		super(MyUserSerializer, self).__init__(*args, **kwargs)
		if self.context['request'].method == "PUT":
			self.fields.pop('password')
