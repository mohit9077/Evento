# Generated by Django 3.1.4 on 2021-01-01 18:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0018_eventregmodel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eventregmodel',
            name='branch',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='eventregmodel',
            name='club',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='eventregmodel',
            name='fname',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='eventregmodel',
            name='lname',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='eventregmodel',
            name='usn',
            field=models.CharField(max_length=100),
        ),
    ]
