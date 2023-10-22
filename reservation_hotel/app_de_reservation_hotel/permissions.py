from rest_framework import permissions

class IsOwnerOrReadOnly(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        
        # Autorise uniquement les propriétaires à modifier les réservations
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.utilisateur == request.user