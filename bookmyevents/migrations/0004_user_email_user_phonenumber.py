# Generated by Django 4.1.7 on 2023-10-26 16:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookmyevents', '0003_payment'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='email',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='user',
            name='phoneNumber',
            field=models.IntegerField(default=0),
        ),
    ]
