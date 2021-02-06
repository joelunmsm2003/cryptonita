from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.utils.html import strip_tags
from django.core import mail
from django.http import JsonResponse
import json
from django.contrib.auth.models import User
from .models import *
from .serializers import *
import requests
from pycoingecko import CoinGeckoAPI
import time
import datetime

@csrf_exempt
def seteaprecio(request):

	monedas = Criptomonedas.objects.all()

	for m in monedas:

		cg = CoinGeckoAPI()

		precio = cg.get_price(ids=m.nombre.lower(), vs_currencies='usd')

		precio=precio[m.nombre.lower()]['usd']

		Historial(fecha=datetime.datetime.now(),price=precio,criptomoneda_id=m.id).save()

		ganancia=Inversion.objects.filter(criptomoneda_id=m.id)

		ganancia_total=[]

		for g in ganancia:

			if g.transaccion=='C':
				signo=1
			else:
				signo=-1

			ganancia_total.insert(1,g.ganancia*signo)

		ganancia_total=sum(ganancia_total)

		HistorialUser(fecha=datetime.datetime.now(),price=precio,criptomoneda_id=m.id,ganancia=ganancia_total).save()

		m.precio=precio

		m.save()

	return JsonResponse(precio, safe=False)



@csrf_exempt
def cryptos(request):

	cg = CoinGeckoAPI()

	listas = cg.get_coins_list()

	suport=cg.get_supported_vs_currencies()

	for s in suport:

		if Criptomonedas.objects.filter(simbolo=s).count()==0:

			Criptomonedas.objects.filter(simbolo=s).update(activo=False)

		else:

			Criptomonedas.objects.filter(simbolo=s).update(activo=True)


	for l in listas:

		if Criptomonedas.objects.filter(nombre=l['id']).count()==0:
			try:
				Criptomonedas(nombre=l['id'],simbolo=l['symbol'],sigla=l['name']).save()
			except:
				pass

	return JsonResponse('precio', safe=False)

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


def takeSecond(elem):
	return elem[4]

@csrf_exempt
def monedas(request,name):

	if request.method == 'GET':

		_historial=Historial.objects.filter(criptomoneda__nombre=name)

		_inversion=Inversion.objects.filter(criptomoneda__nombre=name,eliminado=False).order_by('-id')

		crypto=Criptomonedas.objects.get(nombre=name)

		allcryptos=Criptomonedas.objects.filter(activo=True)

		data=[]
		data_inv=[]
		data_gan=[]

		_in=0

		ganancia_inversion=0
		ganancia_total=0
		cantidad_comprada=0
		balance=0

		# take second element for sort
		
		for i in _inversion:

			elem_gan=[]
			_in=_in+1
			elem_gan.insert(1,_in)
			if i.transaccion=='C':
				signo=1
			else:
				signo=-1

			cantidad_comprada=cantidad_comprada+i.cantidad_comprada*signo

			ganancia_total=ganancia_total+i.ganancia*signo
			elem_gan.insert(2,i.ganancia*signo)
			elem_gan.insert(3,i.porcentaje_ganancia*signo)
			ganancia_inversion=ganancia_inversion+i.ganancia*signo
			elem_gan.insert(4,ganancia_inversion)
			
			timestamp=time.mktime(i.fecha.timetuple())
			elem_gan.insert(5,timestamp*1000)

			#elem_gan.sort(key=takeSecond)


			
			data_gan.insert(1,elem_gan)
			
		data_gan.sort(key=lambda x: x[4])

		data_inv.sort(key=lambda x: x[0])
		data.sort(key=lambda x: x[0])

		
		
		return render(request, 'monedas.html', {'balance':cantidad_comprada*crypto.precio,'title': name,'data':data,'crypto':crypto,'allcryptos':allcryptos,'inversion':data_inv,'cantidad_comprada':round(cantidad_comprada,5),'ganancia':data_gan,'ganancia_total':round(ganancia_total,2)})


@csrf_exempt
def monitor(request):

	if request.method == 'GET':


		_historial=HistorialUser.objects.all().order_by('-id')[:5000]

		_criptos=Criptomonedas.objects.filter(activo=True)

		serializer_cryptos = CriptomonedasSerializer(_criptos, many=True)


		serializer_historial = HistorialUserSerializer(_historial, many=True)

		return render(request, 'inversiones.html', {'title': 'name','allcryptos':_criptos,'cryptos':json.dumps(serializer_cryptos.data),'historial':json.dumps(serializer_historial.data)})


