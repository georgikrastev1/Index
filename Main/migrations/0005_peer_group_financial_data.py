# Generated by Django 3.0.3 on 2020-10-09 22:00

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Main', '0004_auto_20200922_1709'),
    ]

    operations = [
        migrations.CreateModel(
            name='Peer_group_Financial_data',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Peer_group', models.CharField(default='Pulp', max_length=200)),
                ('Market_capitalization', models.FloatField(max_length=50, null=True)),
                ('Market_capitalization_percent', models.FloatField(max_length=50, null=True)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]
