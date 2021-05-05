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
from bs4 import BeautifulSoup
import pandas as pd
@csrf_exempt
def seteaprecio(request):

	monedas = Criptomonedas.objects.all()

	for m in monedas:

		res=requests.get('https://www.coingecko.com/es/monedas/'+m.nombre.lower())
		data = res.text
		soup = BeautifulSoup(data)

		for link in soup.find_all('div', class_='post-body'):
			soup =  BeautifulSoup(str(link))

			for b in soup.find_all('b'):
				valor=b.text


			precio=valor.replace('$','').replace('.','').replace(',','.')

			print('precio',precio)


		if precio:

			if (float(precio)-float(m.precio))*100/float(m.precio) < 50:

				Historial(fecha=datetime.datetime.now(),price=precio,criptomoneda_id=m.id).save()

				m.precio=precio

				m.save()

		'''

		cg = CoinGeckoAPI()

		precio = cg.get_price(ids=m.nombre.lower(), vs_currencies='usd')

		precio=precio[m.nombre.lower()]['usd']
		'''


			

		ganancia=Inversion.objects.filter(criptomoneda_id=m.id)

		ganancia_total=[]

		'''

		for g in ganancia:

			if g.transaccion=='C':
				signo=1
			else:
				signo=-1

			ganancia_total.insert(1,g.ganancia*signo)

		ganancia_total=sum(ganancia_total)

		'''

		#HistorialUser(fecha=datetime.datetime.now(),price=precio,criptomoneda_id=m.id,ganancia=ganancia_total).save()


		

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

def getPrecio(n):
    return n['price']

def getFecha(n):
    return n['fecha']

def takeSecond(elem):
    return elem['fecha']

@csrf_exempt
def monedas(request,name):

	if request.method == 'GET':

		list_medias=[20,480,2000]

		_historial=Historial.objects.filter(criptomoneda__nombre__contains=name).order_by('-id')[:5000]

		serializer_historial = HistorialSerializer(_historial, many=True)

		result = serializer_historial.data

		result.sort(key=takeSecond)

		fechas=list(map(getFecha, result))

		valor=list(map(getPrecio, result))

		data = {'fecha': fechas,'valor': valor}

		df_valor = pd.DataFrame(data,columns=['fecha','valor'])

		df_valor.set_index("fecha", inplace = True)

		_medias=[]

		for lm in list_medias:

			media=[]

			rolling_mean = df_valor.valor.rolling(window=lm).mean()

			for v in rolling_mean.index:
				if str(rolling_mean[v])!='nan':
					media.append({'fecha':v,'valor':rolling_mean[v]})

			_medias.append(media)
		

		try:

			ultimo_hora=(_historial[0].price-_historial[20].price)*100/float(_historial[20].price)

			ultimo_4hora=(_historial[0].price-_historial[80].price)*100/float(_historial[80].price)

			ultimodia=(_historial[0].price-_historial[20*24].price)*100/float(_historial[20*24].price)

		except:

			ultimo_hora=0
			ultimo_4hora=0
			ultimodia=0

		_inversion=Inversion.objects.filter(criptomoneda__nombre__contains=name,eliminado=False,cuenta__nombre='Binance').order_by('id')

		print('name',name)

		crypto=Criptomonedas.objects.get(nombre__contains=name)

		allcryptos=Criptomonedas.objects.filter(activo=True).order_by('-precio')

		data=[]
		data_inv=[]
		data_gan=[]

		_in=0

		ganancia_inversion=0
		ganancia_total=0
		cantidad_comprada=0
		comprada_usd=0
		vendida_usd=0
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

			if signo==1:
				comprada_usd=comprada_usd+i.comprada_usd
			else:
				vendida_usd=vendida_usd+i.comprada_usd

			

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

		
		
		return render(request, 'monedas.html', {'l_list_medias':json.dumps(list_medias),'medias':json.dumps(_medias),'historial':json.dumps(serializer_historial.data),'vendida_usd':round(vendida_usd,3),'ganancia_retorno':round(cantidad_comprada*crypto.precio+round(vendida_usd-comprada_usd,2),3),'comprada_usd':round(comprada_usd,3),'ultimo_hora':round(ultimo_hora,3),'ultimodia':round(ultimodia,3),'ultimo_4hora':round(ultimo_4hora,3),'balance':round(cantidad_comprada*crypto.precio,2),'title': name,'data':data,'crypto':crypto,'allcryptos':allcryptos,'inversion':data_inv,'cantidad_comprada':round(cantidad_comprada,5),'ganancia':data_gan,'inversion_usd':round(vendida_usd-comprada_usd,2)*-1})


@csrf_exempt
def monitor(request):

	if request.method == 'GET':


		total=HistorialUser.objects.all().count()

		_historial=HistorialUser.objects.all().order_by('-id')[:5000]

		_criptos=Criptomonedas.objects.filter(activo=True).order_by('-precio')

		serializer_cryptos = CriptomonedasSerializer(_criptos, many=True)


		serializer_historial = HistorialUserSerializer(_historial, many=True)

		return render(request, 'inversiones.html', {'title': 'name','allcryptos':_criptos,'cryptos':json.dumps(serializer_cryptos.data),'historial':json.dumps(serializer_historial.data)})


@csrf_exempt
def analisis(request):

	if request.method == 'GET':

		cryptos=Criptomonedas.objects.filter(activo=True)

		print(cryptos)


		data=[]

		for c in cryptos:
			ganancia=0
			comprada_usd=0
			porcentaje=0
			vendida_usd=0
			porcentaje_vendida=0

			inv=Inversion.objects.filter(criptomoneda__nombre__contains=c.nombre)
			
			for i in inv:

				if i.transaccion=='C':
					signo=1
				else:
					signo=-1

				ganancia=ganancia+i.ganancia*signo

				if signo==1:
					comprada_usd=comprada_usd+i.comprada_usd
					porcentaje=porcentaje+i.ganancia/i.comprada_usd
				else:
					vendida_usd=vendida_usd+i.comprada_usd
					porcentaje_vendida=porcentaje_vendida+i.ganancia/i.comprada_usd

				
			
			detalle={'moneda':c.nombre,'ganancia':ganancia,'comprada_usd':-vendida_usd+comprada_usd,'porcentaje':porcentaje-porcentaje_vendida}
			data.insert(1,detalle)
			print(data)
			
		return render(request, 'analisis.html', {'data':json.dumps(data)})
