# full_stack_back_exam

Ce projet a pour but de créer une API pour reservation de chambre d'hotel de luxe.
Il est développé avec le Framework Django de Python et une base de données SQLITE.

Pour lancer le projet, lancer les commandes suivantes :

```
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

Le projet est ensuite lancée sur l'url http://127.0.0.1:8000/.
Pour visualiser l'API et l'ensemble de ses composants, aller sur le navigation et naviguer sur les url suivantes :

```
http://127.0.0.1:8000/admin/         => Interface d'administration, identifiants admin admin
http://127.0.0.1:8000/hotels/        => Consulter la table des hotels
http://127.0.0.1:8000/reservations/  => Consulter la table des reservations de l'hotel
http://127.0.0.1:8000/chambres/      => Consulter la table des chambres de l'hotel
http://127.0.0.1:8000/swagger/       => L'interface Swagger permettant de récupérer, modifier créer et supprimer des réservations
```

## Informations supplémentaires

Un compte d'administration a été crée, identifiant admin, pass admin

Une authentification JWT verifie qu'on est bien connecté avant d'afficher les informations
