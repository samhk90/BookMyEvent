# Generated by Django 4.1.7 on 2023-10-10 16:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookmyevents', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bookedBy', models.CharField(max_length=50)),
                ('bookedEvent', models.CharField(max_length=50)),
                ('bookedDate', models.DateField()),
                ('bookedtickets', models.IntegerField()),
                ('bookedprice', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='events',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('eventName', models.CharField(max_length=50)),
                ('eventgenre', models.CharField(max_length=50)),
                ('eventPrice', models.IntegerField()),
                ('eventImage', models.ImageField(upload_to='images/')),
                ('eventDate', models.DateField()),
                ('numberOfTickets', models.IntegerField()),
            ],
        ),
    ]
