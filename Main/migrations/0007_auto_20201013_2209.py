# Generated by Django 3.0.3 on 2020-10-13 20:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Main', '0006_peer_group_lists'),
    ]

    operations = [
        migrations.AlterField(
            model_name='peer_group_financial_data',
            name='Peer_group',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Main.Peer_group_lists'),
        ),
    ]