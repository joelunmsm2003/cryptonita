from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from api.views import *
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('api.urls')),
	url(r'^seteaprecio/', seteaprecio),
	url(r'^email/', email),
    url(r'^analisis/', analisis),
	url(r'^confirmacion/(\w+)', confirmacion),
    url(r'^health_check/', include('health_check.urls')),
    url(r'^api/token/$', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    url(r'^api/token/refresh/$', TokenRefreshView.as_view(), name='token_refresh'),
    url(r'^email/', email),
    url(r'^monedas/(\w+)', monedas),
    url(r'^cryptos', cryptos),
    url(r'^monitor', monitor),
    url(r'^alerta/(\w+)', alerta),
    url(r'^historical/(\w+)', historical),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

