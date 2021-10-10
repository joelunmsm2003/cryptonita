# Cryptonita 

An application to manage and track your cryptocurrency investments locally on your computer with the Django framework without using any centralized application to track your investments.


![alt text for screen readers](https://i.postimg.cc/vTPp2HvQ/Screenshot-2021-10-10-T113022-132.png "Cryptocurrencies List ").


## Requirements

Docker

## Build and Run application

```
docker-compose build


```

```

docker-compose up

```
## Commands

Run database migrations
```
docker-compose run web python manage.py makemigrations


```

```

docker-compose run web python manage.py migrate

```
Create admin user
```
docker-compose run web python manage.py createsuperuser --username admin

```

Load cryptos 
```
http://localhost:5500/getCrypto

```


Once the server is running, visit http://127.0.0.1:5500/admin in your web browser. Now, you should see something 


