from rest_framework import serializers
from kgcoin.models import Kgcoin, CoinTransaction
from wallet.models import Wallet
from wallet.serializers import UserForUseSerializer
from rest_framework.response import Response
from rest_framework import filters, status


class KgcoinSerializer(serializers.ModelSerializer):

    class Meta:
        model = Kgcoin
        fields = '__all__'


class WalletForTransactionSerializer(serializers.ModelSerializer):
    user = UserForUseSerializer(read_only=True)

    class Meta:
        model = Wallet
        fields = ('id', 'user', 'account_number')


class CoinTransactionSerializer(serializers.ModelSerializer):

    class Meta:
        model = CoinTransaction
        fields = '__all__'

    