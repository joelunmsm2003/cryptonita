# Cryptonyta 

An application to manage and track investments in cryptocurrencies


## Requirements

Docker

## Build and Run application

```
docker-compose build
docker-compose up

```
## Commands

Run database migrations
```
docker-compose run web python manage.py makemigrations
docker-compose run web python manage.py migrate

```
Create admin user
```
docker-compose run web python manage.py createsuperuser --username admin

```

Load cryptos
```
curl http://localhost:5500/getPrecio

```


Once the server is running, visit http://127.0.0.1:5500/ in your web browser. Now, you should see something 


