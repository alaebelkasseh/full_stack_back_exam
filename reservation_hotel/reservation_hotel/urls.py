"""
URL configuration for reservation_hotel project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework.routers import DefaultRouter
from app_de_reservation_hotel.views import HotelViewSet
from app_de_reservation_hotel.views import ReservationViewSet
from app_de_reservation_hotel.views import ChambreViewSet
from app_de_reservation_hotel.swagger import schema_view


router = DefaultRouter()

router.register(r'hotels', HotelViewSet)
router.register(r'reservations', ReservationViewSet)
router.register(r'chambres', ChambreViewSet)

urlpatterns = [

    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    #path('api/', include('reservations.urls')),
]

urlpatterns += router.urls

