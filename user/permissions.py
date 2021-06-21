from django.contrib.auth.models import AnonymousUser
from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsUserOwnerOrReadOnly(BasePermission):
    
    def has_object_permission(self, request, view, obj):
        if request.method == 'GET':
            return True
        return obj == request.user


class IsStaffOrCreateUser(BasePermission):
    
    def has_object_permission(self, request, view, obj):
        if request.method == 'GET':
            return True
        else:
            return request.user.is_superuser or request.user.is_staff