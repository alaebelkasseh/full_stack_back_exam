from rest_framework import serializers
from .models import Reservation

class ReservationSerializer(serializers.ModelSerializer):

    class Meta:

        model = Reservation

        fields = '__all__

class ChambreSerializer(serializers.ModelSerializer):

    class Meta:

        model = Chambre

        fields = '__all__