from django.shortcuts import render
from django.db import transaction
from rest_framework import filters
from rest_framework import viewsets
from wallet.serializers import TransactionSerializer, CategorySerializer, WalletSerializer
from wallet.models import Transaction, Category, Wallet
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser
from .permissions import IsMyAdmin, IsOwner, IsTransactionOwner


class CategoryView(viewsets.ModelViewSet):
	queryset = Category.objects.all()
	serializer_class = CategorySerializer
	permission_classes = (IsMyAdmin, )


class WalletView(viewsets.ModelViewSet):
	serializer_class = WalletSerializer
	permission_classes = (IsAuthenticatedOrReadOnly, IsMyAdmin)

	def get_queryset(self):
		user = self.request.user
		return Wallet.objects.filter(user=user)


class TransactionView(viewsets.ModelViewSet):
	queryset = Transaction.objects.prefetch_related('sender_wallet', 'reciever_wallet', 'transactions').all()
	serializer_class = TransactionSerializer
	permission_classes = (IsTransactionOwner, )

	def get_queryset(self):
		user = self.request.user.wallet_owner
		return Transaction.objects.filter(sender=user.id) or Transaction.objects.filter(reciever=user.id)


# import operator
# import calendar
# import datetime
# import time


# def prev_month_range(when = None):
# 	"""Return (previous month's start date, previous month's end date)."""
# 	if not when:
# 		# Default to today.
# 		when = datetime.datetime.today()
# 	# Find previous month: http://stackoverflow.com/a/9725093/564514
# 	# Find today.
# 	first = datetime.date(day=1, month=when.month, year=when.year)
# 	# Use that to find the first day of this month.
# 	prev_month_end = first - datetime.timedelta(days=1)
# 	prev_month_start = datetime.date(day=1, month= prev_month_end.month, year= prev_month_end.year)
# 	# Return previous month's start and end dates in YY-MM-DD format.
# 	return {'start': prev_month_start, 'end':prev_month_end}


# def prev_year_range(when = None):
# 	"""Returns the previous year range from Jan 1 to Dec 31"""
# 	if not when:
# 		# Default to today.
# 		when = datetime.datetime.today()
# 		# Find today.
# 	prev_year = when.year - 1
# 	# Use that to find the first day of this month.
# 	first_day_year = datetime.date(day=1, month=1, year=prev_year)
# 	last_day_year = datetime.date(day=31, month=12, year=prev_year)
# 	# Return previous month's start and end dates in YY-MM-DD format.
# 	return {'start': first_day_year, 'end': last_day_year}


# def last_30_days():
# 	return datetime.datetime.today() + datetime.timedelta(-30)


# def transaction_search(request):

# 	user = request.user
# 	wallet = request.GET.get('wallet')
# 	income = request.GET.get('income')
# 	outcome = request.GET.get('outcome')
# 	date = request.GET.get('date')

# 	transactions = Transaction.objects.filter(wallet__user=user)

# 	if wallet:
# 		transactions = transactions.filter(wallet = wallet)

# 	if date:
# 		if 'range' in date:
# 			date = date.split('.')
# 			date[0] = date[0].replace('range', '')
# 			transactions = transactions.filter(date__range = date)
		
# 		elif date == 'prev_year':
		
# 			prev_year = prev_year_range()
# 			transactions = transactions.filter(date__range = [prev_year['start'], prev_year['end']])
		
# 		elif date == 'prev_month':
		
# 			prev_month = prev_month_range()
# 			transactions = transactions.filter(date__range = [prev_month['start'], prev_month['end']])
		
# 		elif date == 'current_year':
		
# 			today = datetime.datetime.today()
# 			last_date = datetime.date(today.year, 12, 31)
# 			first_date = datetime.date(today.year, 1, 1)            
# 			transactions = transactions.filter(date__range = [first_date, last_date])        
		
# 		elif date == 'current_month':
		
# 			today = datetime.datetime.today()
# 			last_date = calendar.monthrange(today.year, today.month)[1]
# 			last_date = datetime.date(today.year, today.month, last_date)
# 			first_date = datetime.date(today.year, today.month, 1)

# 			transactions = transactions.filter(date__range = [first_date, last_date])

# 	return transactions