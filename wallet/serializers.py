from rest_framework import serializers
from wallet.models import Wallet, Transaction, Category
from user.models import User

class UserForUseSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = ('first_name', 'last_name')


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ('name', )


class WalletSerializer(serializers.ModelSerializer):
    user = UserForUseSerializer(read_only=True)

    class Meta:
        model = Wallet
        fields = '__all__'


class TransactionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Transaction
        fields = '__all__'

    def create(self, validated_data):
        sender_data = validated_data.get('sender')
        reciever_data = validated_data.get('reciever')
        amount = validated_data.get('amount')
        category_data = validated_data.get('category')
        category = Category.objects.get(pk=category_data.id)
        if sender_data is None:
            reciever = Wallet.objects.get(pk=reciever_data.id)
            deposit = Transaction.objects.create(reciever=reciever, amount=amount, category=category)
            deposit.transfer()
            return deposit
        elif reciever_data is None:
            sender = Wallet.objects.get(pk=sender_data.id)
            withdraw = Transaction.objects.create(sender=sender, amount=amount, category=category)
            withdraw.transfer()
            return withdraw
        reciever = Wallet.objects.get(pk=reciever_data.id)
        sender = Wallet.objects.get(pk=sender_data.id)
        reference = validated_data.get('reference_id')
        transaction = Transaction.objects.create(sender=sender, reciever=reciever, amount=amount, category=category, reference_id=reference)
        transaction.transfer()
        return transaction
