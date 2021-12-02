from django.shortcuts import render
from rest_framework import viewsets, permissions
from .models import *
from .serializers import *
from django.views.decorators.csrf import csrf_exempt
from rest_framework.permissions import AllowAny, IsAdminUser


class MyUserViewSet(viewsets.ModelViewSet):
    queryset = MyUser.objects.all()
    serializer_class = MyUserSerializer
    permission_classes = [AllowAny]

class CryptocurrencyViewSet(viewsets.ModelViewSet):
    queryset = Cryptocurrency.objects.all()
    serializer_class = CryptocurrencySerializer
    permission_classes = [AllowAny]

    def list(self, request, *args, **kwargs):
        response = super().list(request, args, kwargs)

        table=Generic.objects.filter(table='Cryptocurrency')
        file_fields=[]
        for t in table:
            file_fields.append({'field':t.column,'type':t.datatype,'visible':t.visible,'editable':t.editable,'icon':t.icon,'label':t.label,'editable':t.editable})


        response.data['meta'] = file_fields

        return response

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

class AccountsViewSet(viewsets.ModelViewSet):
    queryset = Account.objects.all()
    serializer_class = AccountsSerializer
    permission_classes = [AllowAny]

class GenericViewSet(viewsets.ModelViewSet):
    queryset = Generic.objects.all()
    serializer_class = GenericSerializer
    permission_classes = [AllowAny]
