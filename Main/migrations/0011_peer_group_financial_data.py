# Generated by Django 3.0.3 on 2020-10-13 20:31

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Main', '0010_delete_peer_group_financial_data'),
    ]

    operations = [
        migrations.CreateModel(
            name='Peer_group_Financial_data',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Market_capitalization', models.FloatField(max_length=50, null=True)),
                ('Market_capitalization_percent', models.FloatField(max_length=50, null=True)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('Peer_group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Main.Peer_group_lists')),
            ],
        ),
    ]
