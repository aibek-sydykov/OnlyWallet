# Generated by Django 3.2.3 on 2021-07-07 14:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('kgcoin', '0003_alter_kgcoin_name'),
        ('wallet', '0015_wallet_kgcoin_amount'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='wallet',
            name='kgcoin_amount',
        ),
        migrations.CreateModel(
            name='KgCoinIhfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=2, default=0, max_digits=12, verbose_name='Количество монеты')),
                ('kgcoin', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='kgcoin.kgcoin')),
            ],
        ),
        migrations.AddField(
            model_name='wallet',
            name='kgcoin_info',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='kgcoin_info', to='wallet.kgcoinihfo'),
        ),
    ]
