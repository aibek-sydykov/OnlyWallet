# Generated by Django 3.2.3 on 2021-07-05 19:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wallet', '0013_alter_transaction_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='amount',
            field=models.IntegerField(default=0, verbose_name='Сумма'),
        ),
        migrations.AlterField(
            model_name='wallet',
            name='current_balance',
            field=models.IntegerField(default=0, verbose_name='Баланс счета'),
        ),
    ]
