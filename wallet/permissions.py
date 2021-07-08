from django.contrib.auth.models import AnonymousUser
from rest_framework.permissions import BasePermission


class IsMyAdmin(BasePermission):

    def has_permission(self, request, view):
        if request.method == 'GET':
            return True
        return False
    
    def has_object_permission(self, request, view, obj):
        if request.method == 'GET':
            return True
        return False


class IsOwner(BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.method == 'GET':
            return obj.user == request.user
        return request.user.is_superuser or request.user.is_staff


class IsTransactionOwner(BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.method == 'DELETE' or request.method == 'UPDATE':
            return False
        elif request.user.wallet_owner == obj.sender:
            return True
        elif request.user.wallet_owner == obj.reciever:
            return True 
        return request.user.is_superuser or request.user.is_staff
        