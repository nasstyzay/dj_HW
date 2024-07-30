from rest_framework.permissions import BasePermission
from rest_framework.exceptions import PermissionDenied
from .models import Advertisement

class IsAuthorOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        if view.action in ['create', 'update', 'partial_update', 'destroy']:
            return request.user.is_authenticated
        return True

    def has_object_permission(self, request, view, obj):
        if view.action in ['update', 'partial_update', 'destroy']:
            return obj.author == request.user
        return True

class CanCreateAdvertisement(BasePermission):
    def has_permission(self, request, view):
        if view.action == 'create':
            if Advertisement.objects.filter(author=request.user, status='OPEN').count() >= 10:
                raise PermissionDenied('You cannot have more than 10 open advertisements.')
        return True
