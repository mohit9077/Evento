# Generated by Django 3.1.4 on 2021-01-12 21:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0019_auto_20210101_2353'),
    ]

    operations = [
        migrations.AddField(
            model_name='eventregmodel',
            name='event_title',
            field=models.CharField(default='NULL', max_length=100),
        ),
        migrations.AlterField(
            model_name='eventregmodel',
            name='branch',
            field=models.CharField(default='NULL', max_length=100),
        ),
        migrations.AlterField(
            model_name='eventregmodel',
            name='club',
            field=models.CharField(default='NULL', max_length=100),
        ),
        migrations.AlterField(
            model_name='eventregmodel',
            name='fname',
            field=models.CharField(default='NULL', max_length=100),
        ),
        migrations.AlterField(
            model_name='eventregmodel',
            name='lname',
            field=models.CharField(default='NULL', max_length=100),
        ),
        migrations.AlterField(
            model_name='eventregmodel',
            name='usn',
            field=models.CharField(default='NULL', max_length=100),
        ),
    ]
