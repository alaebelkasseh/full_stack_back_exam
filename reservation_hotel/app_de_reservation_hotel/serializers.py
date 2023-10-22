from rest_framework import serializers
from .models import Hotel
from .models import Reservation
from .models import Chambre

class HotelSerializer(serializers.ModelSerializer):

    class Meta:

        model = Hotel
        fields = '__all__'

class ReservationSerializer(serializers.ModelSerializer):

    class Meta:

        model = Reservation
        fields = '__all__'

class ChambreSerializer(serializers.ModelSerializer):

    class Meta:

        model = Chambre
        fields = '__all__'