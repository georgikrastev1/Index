# Generated by Django 3.0.3 on 2020-10-13 19:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Main', '0005_peer_group_financial_data'),
    ]

    operations = [
        migrations.CreateModel(
            name='Peer_group_lists',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Group_name', models.CharField(default='Pulp', max_length=200)),
                ('Group_description', models.CharField(max_length=400)),
            ],
        ),
    ]
