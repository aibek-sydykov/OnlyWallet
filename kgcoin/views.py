from django.shortcuts import render
from kgcoin.models import Kgcoin, CoinTransaction
from kgcoin.serializers import KgcoinSerializer, CoinTransactionSerializer
from rest_framework import viewsets
from wallet.permissions import IsMyAdmin
from kgcoin.permissions import IsCoinTransactionOwner
from rest_framework.response import Response
from rest_framework import status
from wallet.models import Wallet


class KgcoinView(viewsets.ModelViewSet):
    queryset = Kgcoin.objects.all()
    serializer_class = KgcoinSerializer
    permission_classes = (IsMyAdmin, ) 


class CoinTransactionView(viewsets.ModelViewSet):
    queryset = CoinTransaction.objects.all()
    serializer_class = CoinTransactionSerializer
    permission_classes = (IsCoinTransactionOwner, ) 

    def get_queryset(self):
        user = self.request.user.wallet_owner
        return CoinTransaction.objects.filter(user_wallet=user.id)

    def create(self, request, *args, **kwargs):
        user = request.user
        buy_data = request.data.get('buy_amount')
        sell_data = request.data.get('sell_amount')
        kgcoin_data = request.data.get('kgcoin')
        kgcoin = Kgcoin.objects.get(pk=kgcoin_data)
        user_wallet_data = request.data.get('user_wallet')
        user_wallet= Wallet.objects.get(pk=user_wallet_data)
        if sell_data is not None and buy_data is not None:
            return Response('Ошибка. Выберете что-то одно: Покупка или продажа монеты', status=status.HTTP_403_FORBIDDEN)
        elif buy_data is None:
            sell_int = int(sell_data)
            sell_coin = CoinTransaction.objects.create(user_wallet=user_wallet, kgcoin=kgcoin, sell_amount=sell_int)
            sell_coin.transfer_coin()
            return Response(f'Продажа монет на сумму {sell_int * kgcoin.cost} сом успешно совершена', status=status.HTTP_201_CREATED)
        elif sell_data is None:
            buy_int = int(buy_data)
            if buy_int >= kgcoin.amount:
                return Response('Данная операция недоступна', status=status.HTTP_403_FORBIDDEN)
            elif user_wallet.current_balance < buy_int * kgcoin.cost: 
                return Response('У вас недостаточно средств для данной покупки', status=status.HTTP_403_FORBIDDEN)
            buy_coin = CoinTransaction.objects.create(user_wallet=user_wallet, kgcoin=kgcoin, buy_amount=buy_int)
            buy_coin.transfer_coin()
            return Response(f'Покупка монет на сумму {buy_int * kgcoin.cost} сом успешно совершена', status=status.HTTP_201_CREATED)
        return super().create(request, *args, **kwargs)