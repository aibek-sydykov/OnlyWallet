# Generated by Django 3.2.3 on 2021-07-05 15:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0005_delete_company'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='patronymic',
            field=models.CharField(blank=True, max_length=250, null=True, verbose_name='Отчество'),
        ),
    ]
