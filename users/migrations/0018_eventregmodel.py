# Generated by Django 3.1.4 on 2021-01-01 18:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0017_auto_20210101_2216'),
    ]

    operations = [
        migrations.CreateModel(
            name='eventregmodel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=20)),
                ('lname', models.CharField(max_length=20)),
                ('usn', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('branch', models.CharField(max_length=40)),
                ('club', models.CharField(max_length=20)),
            ],
        ),
    ]