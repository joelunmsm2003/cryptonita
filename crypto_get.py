import requests

url='http://app01.comunica7.com:5500/seteaprecio'

response=requests.get(url)

print(response.text)