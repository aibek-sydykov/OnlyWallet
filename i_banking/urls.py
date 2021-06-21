from django.contrib import admin
from django.urls import path
from rest_auth.views import LoginView
from rest_auth.registration.views import RegisterView
from user.views import UserView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', LoginView.as_view(), name='rest_login'),
    path('register/', RegisterView.as_view(), name='rest_register'),
    path('user/<int:pk>', UserView.as_view({'get': 'retrieve', 'put': 'update'})),
]
