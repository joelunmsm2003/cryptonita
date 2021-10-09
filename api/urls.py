from django.urls import path, include
from rest_framework import routers
from django.contrib import admin
from .api import *
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


router = routers.DefaultRouter()


router.register('api/v1/cryptos', CriptomonedasViewSet, 'cryptos')
router.register('api/v1/inversiones', InversionViewSet, 'inversiones')
router.register(r'api/v1/historial/(?P<username>.+)', HistorialViewSet, 'historial')

admin.site.site_header = 'Cryptonita'



urlpatterns = [
	path('', include(router.urls)),
	path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
	path(r'^health_check/', include('health_check.urls')),
	path(r'^api/token/$', TokenObtainPairView.as_view(), name='token_obtain_pair'),
	path(r'^api/token/refresh/$', TokenRefreshView.as_view(), name='token_refresh'),

]