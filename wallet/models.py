from django.conf import settings
from django.db import models
import datetime
from django.db import IntegrityError


class Category(models.Model):
	name = models.CharField('name', max_length=90)

	class Meta:
		verbose_name = 'Категория'
		verbose_name_plural = 'Категории'

	def __str__(self):
		return self.name


class Wallet(models.Model):

	user = models.OneToOneField(settings.AUTH_USER_MODEL, models.CASCADE, related_name='wallet_owner')
	account_number = models.CharField('Номер счета', max_length=255)
	current_balance = models.FloatField('Баланс счета', default=0)
	created_at = models.DateTimeField('Дата создания кошелька', auto_now_add=True)
	amount = models.FloatField('Количество монеты', default = 0)

	class Meta:
		verbose_name = 'Кошелек'
		verbose_name_plural = 'Кошельки'

	def __str__(self):
		return str(self.account_number)


class Transaction(models.Model):
	sender = models.ForeignKey(Wallet, models.CASCADE, 'sender_wallet', blank=True, null=True)
	reciever = models.ForeignKey(Wallet, models.CASCADE, 'reciever_wallet', blank=True, null=True)
	amount = models.FloatField('Сумма', default=0)
	category = models.ForeignKey(Category, models.CASCADE, 'transactions')
	date = models.DateField('Дата создания транзакции', auto_now_add=True)
	reference_id = models.CharField('Реферальный код', max_length=255, blank=True, null=True)

	class Meta:
		verbose_name = 'Транзакция'
		verbose_name_plural = 'Транзакции'

	def __str__(self):
		return '%s сом (%s)' % (self.amount, self.category)

	def transfer(self):
		if self.sender and self.reciever:
			self.sender.current_balance -= self.amount
			self.reciever.current_balance += self.amount
			self.sender.save() 
			self.reciever.save()
		elif self.sender == None:
			self.reciever.current_balance += self.amount
			return self.reciever.save()
		elif self.reciever == None:
			self.sender.current_balance -= self.amount 
			return self.sender.save()