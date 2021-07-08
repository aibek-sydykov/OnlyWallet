from django.db import models


class Kgcoin(models.Model):
	amount = models.FloatField('Количество монеты', default = 0)
	cost = models.FloatField('Стоимость монеты', default = 100)

	class Meta:
		verbose_name = 'KGcoin'
		verbose_name_plural = 'KGcoins'

	def __str__(self):
		return 'KG Coin'

class CoinTransaction(models.Model):
	user_wallet = models.ForeignKey('wallet.Wallet', models.CASCADE, 'wallet_owner')
	kgcoin = models.ForeignKey(Kgcoin, models.CASCADE, 'kgcoin')
	buy_amount = models.FloatField('Покупка монеты', default = 0)
	sell_amount = models.FloatField('Продажа монеты', default = 0)
	date = models.DateField('Дата создания транзакции', auto_now_add=True)

	class Meta:
		verbose_name = 'Coin транзакция'
		verbose_name_plural = 'Coin транзакции'

	def __str__(self):
		return f'{self.user_wallet} - {self.user_wallet.amount} '
	
	def transfer_coin(self):
		if self.sell_amount == 0:
			price = self.buy_amount * self.kgcoin.cost
			self.user_wallet.current_balance -= price
			self.user_wallet.amount += self.buy_amount
			self.user_wallet.save()
			self.kgcoin.amount -= self.buy_amount
			profit = self.kgcoin.cost * 0.001 * self.buy_amount
			self.kgcoin.cost += profit
			self.kgcoin.save()
		if self.buy_amount == 0:
			price = self.sell_amount * self.kgcoin.cost
			self.user_wallet.current_balance += price
			self.user_wallet.amount -= self.sell_amount
			self.user_wallet.save()
			self.kgcoin.amount += self.sell_amount
			loss = self.kgcoin.cost * 0.0005 * self.sell_amount
			self.kgcoin.cost -= loss
			self.kgcoin.save()




