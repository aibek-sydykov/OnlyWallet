# Generated by Django 3.2.3 on 2021-07-07 16:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wallet', '0018_alter_kgcoinihfo_wallet'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='wallet',
            name='kgcoin_info',
        ),
        migrations.AddField(
            model_name='wallet',
            name='amount',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=12, verbose_name='Количество монеты'),
        ),
        migrations.DeleteModel(
            name='KgCoinIhfo',
        ),
    ]