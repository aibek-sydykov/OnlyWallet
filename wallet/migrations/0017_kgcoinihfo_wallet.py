# Generated by Django 3.2.3 on 2021-07-07 14:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wallet', '0016_auto_20210707_2000'),
    ]

    operations = [
        migrations.AddField(
            model_name='kgcoinihfo',
            name='wallet',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='wallet_owner', to='wallet.wallet'),
        ),
    ]
