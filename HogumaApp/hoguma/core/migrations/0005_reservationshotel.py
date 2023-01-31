# Generated by Django 4.1.5 on 2023-01-30 23:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_reservationsrestaurant_email'),
    ]

    operations = [
        migrations.CreateModel(
            name='reservationsHotel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('typeRoom', models.CharField(max_length=50)),
                ('entry_date', models.DateField()),
                ('departure_date', models.DateField()),
            ],
        ),
    ]
