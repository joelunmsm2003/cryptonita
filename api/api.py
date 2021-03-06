from django.shortcuts import render
from rest_framework import viewsets, permissions
from .models import *
from .serializers import *
from django.views.decorators.csrf import csrf_exempt
from rest_framework.permissions import AllowAny, IsAdminUser


class CryptocurrencyViewSet(viewsets.ModelViewSet):
    queryset = Cryptocurrency.objects.all()
    serializer_class = CryptocurrencySerializer
    permission_classes = [AllowAny]

class HistorialViewSet(viewsets.ModelViewSet):
    queryset = Historial.objects.all()
    serializer_class = HistorialSerializer
    permission_classes = [AllowAny]


    def get_queryset(self):

        name = self.request.query_params.get('username', None)

        _historial=Historial.objects.filter(criptomoneda__nombre__contains=name).order_by('-id')[:1]

        print('username',_historial)
        """
        This view should return a list of all the purchases for
        the user as determined by the username portion of the URL.
        """
        
        return Historial.objects.filter(criptomoneda__nombre__contains=name)


class TransactionViewSet(viewsets.ModelViewSet):
    queryset = Transaction.objects.all()
    serializer_class = TransactionsSerializer
    permission_classes = [AllowAny]

