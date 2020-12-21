from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.utils.html import strip_tags
from django.core import mail
from django.http import JsonResponse
import json
from django.contrib.auth.models import User
from .models import *
import requests
from pycoingecko import CoinGeckoAPI



@csrf_exempt
def seteaprecio(request):

	monedas = Criptomonedas.objects.all()

	for m in monedas:

		cg = CoinGeckoAPI()

		precio = cg.get_price(ids=m.nombre.lower(), vs_currencies='usd')

		precio=precio[m.nombre.lower()]['usd']

		m.precio=precio

		m.save()

	return JsonResponse(precio, safe=False)


@csrf_exempt
def email(request):

	if request.method == 'POST':


		email=json.loads(request.body)['email']

		user = MyUser.objects.create_user(email, email,email)




		subject = 'QAPLA Registro'
		confirma='http://localhost:5000/confirmacion/'+str(user.id)
		html='<img src="https://www.sistemaimpulsa.com/blog/wp-content/uploads/2019/10/2-30.jpg"><br><br> Bienvenido a Qapla haz click en el link para registrarte '+confirma
		
		plain_message = strip_tags(html)
		from_email = 'From <byteindie@gmail.com>'
		to = email

		mail.send_mail(subject, plain_message, from_email, [to], html_message=html)

		return JsonResponse('ok', safe=False)


@csrf_exempt
def confirmacion(request,id):

	if request.method == 'GET':


		_user=MyUser.objects.get(id=id)
		_user.confirma_email=True
		_user.save()

		return JsonResponse('ok', safe=False)
