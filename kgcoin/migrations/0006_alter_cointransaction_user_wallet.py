# Generated by Django 3.2.3 on 2021-07-07 16:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wallet', '0019_auto_20210707_2221'),
        ('kgcoin', '0005_remove_kgcoin_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cointransaction',
            name='user_wallet',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='wallet.wallet'),
        ),
    ]