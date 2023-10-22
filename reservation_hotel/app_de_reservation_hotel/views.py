from django.shortcuts import render

from rest_framework import viewsets
from .models import Reservation
from .models import Chambre
from .serializers import ReservationSerializer
from .serializers import ChambreSerializer

class ReservationViewSet(viewsets.ModelViewSet):

    queryset = Reservation.objects.all()

    serializer_class = ReservationSerializer

class ChambreViewSet(viewsets.ModelViewSet):

    queryset = Reservation.objects.all()

    serializer_class = ChambreSerializer