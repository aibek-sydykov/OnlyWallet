from django.contrib.auth.models import AnonymousUser
from rest_framework.permissions import BasePermission


class IsCoinTransactionOwner(BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.method == 'DELETE' or request.method == 'UPDATE':
            return False
        elif request.user.wallet_owner == obj.user_wallet:
            return True
        return request.user.is_superuser or request.user.is_staff