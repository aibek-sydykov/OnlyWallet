from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from user.models import User
from user.serializers import UserSerializer
from user.permissions import IsUserOwnerOrReadOnly

class UserView(ModelViewSet):
    queryset = User.objects.prefetch_related('wallet_owner').all()
    serializer_class = UserSerializer
    lookup_field = 'pk'
    permission_classes = (IsUserOwnerOrReadOnly,) 
