# Generated by Django 3.0.5 on 2021-01-15 13:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0020_auto_20210113_0252'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eventregmodel',
            name='email',
            field=models.EmailField(default='NULL', max_length=254),
        ),
    ]
