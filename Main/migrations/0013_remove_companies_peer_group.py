# Generated by Django 3.0.3 on 2020-10-13 20:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Main', '0012_companies_peer_group_2'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='companies',
            name='Peer_group',
        ),
    ]
