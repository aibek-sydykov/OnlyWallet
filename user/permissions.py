from django.contrib.auth.models import AnonymousUser
from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsUserOwnerOrReadOnly(BasePermission):
    
    def has_object_permission(self, request, view, obj):
        if obj == request.user:
            return True
        return request.user.is_superuser or request.user.is_staff
