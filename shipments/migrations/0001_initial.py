# Generated by Django 2.2.20 on 2021-04-22 10:31

from django.db import migrations, models
import django_countries.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Shipment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tracking_number', models.CharField(max_length=50)),
                ('receiver_name', models.CharField(max_length=50)),
                ('receiver_address', models.CharField(max_length=120)),
                ('receiver_city', models.CharField(max_length=50)),
                ('receiver_state', models.CharField(max_length=50)),
                ('receiver_country', django_countries.fields.CountryField(max_length=2)),
            ],
        ),
    ]