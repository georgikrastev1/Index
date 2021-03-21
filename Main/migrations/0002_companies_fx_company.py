# Generated by Django 3.0.3 on 2020-09-21 20:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='companies',
            name='Fx_company',
            field=models.CharField(choices=[('AUD', 'AUD'), ('BRL', 'BRL'), ('CNY', 'CNY'), ('GBP', 'GBP'), ('HKD', 'HKD'), ('JPY', 'JPY'), ('NOK', 'NOK'), ('SEK', 'SEK'), ('USD', 'USD'), ('CLP', 'CLP'), ('ZAR', 'ZAR'), ('IDR', 'IDR'), ('THB', 'THB'), ('PLN', 'PLN'), ('INR', 'INR'), ('ILS', 'ILS'), ('EUR', 'EUR')], default='EUR', max_length=200),
        ),
    ]
