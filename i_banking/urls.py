from django.contrib import admin
from django.urls import path
from rest_auth.views import LoginView
from rest_auth.registration.views import RegisterView
from user.views import UserView
from wallet.views import TransactionView, CategoryView, WalletView
from kgcoin.views import KgcoinView, CoinTransactionView
from django.conf.urls import include
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('transactions', TransactionView, basename='transactions')
router.register('category', CategoryView, basename='category')
router.register('wallet', WalletView, basename='wallet')
router.register('kgcoin', KgcoinView, basename='kgcoin')
router.register('kgcoin_transactions', CoinTransactionView, basename='kgcoin_transactions')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', LoginView.as_view(), name='rest_login'),
    path('register/', RegisterView.as_view(), name='rest_register'),
    path('user/<int:pk>', UserView.as_view({'get': 'retrieve', 'put': 'update'})),
    path('', include(router.urls))
]
