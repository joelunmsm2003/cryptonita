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


class InversionViewSet(viewsets.ModelViewSet):
    queryset = Inversion.objects.all()
    serializer_class = InversionsSerializer
    permission_classes = [AllowAny]

