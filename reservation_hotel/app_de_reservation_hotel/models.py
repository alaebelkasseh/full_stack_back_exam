from django.db import models

class Reservation(models.Model):

    nom = models.CharField(max_length=100)

    date_d_arrivee = models.DateField()

    date_de_depart = models.DateField()

    chambre = models.CharField(max_length=10)

    class Meta:
        app_label = 'app_de_reservation_hotel'
    
class Chambre(models.Model):

    numero = models.CharField(max_length=10)

    type = models.CharField(max_length=100)

    class Meta:
        app_label = 'app_de_reservation_hotel'



