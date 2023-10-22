from django.shortcuts import render

from rest_framework import viewsets
from .models import Reservation
from .models import Chambre
from .serializers import ReservationSerializer
from .serializers import ChambreSerializer
from .permissions import IsOwnerOrReadOnly

class ReservationViewSet(viewsets.ModelViewSet):

    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer
    permission_classes = [IsOwnerOrReadOnly] 

class ChambreViewSet(viewsets.ModelViewSet):

    queryset = Chambre.objects.all()
    serializer_class = ChambreSerializer
    permission_classes = [IsOwnerOrReadOnly] 