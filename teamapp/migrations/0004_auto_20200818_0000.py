# Generated by Django 3.0.9 on 2020-08-17 21:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teamapp', '0003_auto_20200814_1618'),
    ]

    operations = [
        migrations.AddField(
            model_name='list',
            name='address',
            field=models.CharField(max_length=150, null=True, verbose_name='Адрес ресторана'),
        ),
        migrations.AddField(
            model_name='list',
            name='mailbox',
            field=models.EmailField(max_length=100, null=True, verbose_name='E-mail'),
        ),
    ]
