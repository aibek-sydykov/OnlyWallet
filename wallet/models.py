from django.db import models
from django.conf import settings


class Wallet(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, models.CASCADE, 'wallet_owner')
    personal_account = models.IntegerField('Номер лицевого счета')
    current_balance = models.IntegerField('Баланс', default=0)
    created_at = models.DateTimeField('Дата создания', auto_now_add=True)

