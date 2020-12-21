from django.shortcuts import render
from rest_framework import viewsets, permissions
from .models import *
from .serializers import *
from django.views.decorators.csrf import csrf_exempt
from rest_framework.permissions import AllowAny, IsAdminUser


class CriptomonedasViewSet(viewsets.ModelViewSet):
    queryset = Criptomonedas.objects.all()
    serializer_class = CriptomonedasSerializer
    permission_classes = [AllowAny]


class InversionViewSet(viewsets.ModelViewSet):
    queryset = Inversion.objects.all()
    serializer_class = InversionsSerializer
    permission_classes = [AllowAny]


class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

class MedidasViewSet(viewsets.ModelViewSet):
    queryset = Medidas.objects.all()
    serializer_class = MedidasSerializer


class SubcategoriaViewSet(viewsets.ModelViewSet):
    queryset = Subcategoria.objects.all()
    serializer_class = SubcategoriaSerializer


class CategoriaViewSet(viewsets.ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer


class FavoritosViewSet(viewsets.ModelViewSet):
    queryset = Favoritos.objects.all()
    serializer_class = FavoritosSerializer


class CercademiViewSet(viewsets.ModelViewSet):
    queryset = Cercademi.objects.all()
    serializer_class = CercademiSerializer

class PromocionViewSet(viewsets.ModelViewSet):
    queryset = Promocion.objects.all()
    serializer_class = PromocionSerializer

