# Generated by Django 3.0.5 on 2020-12-18 22:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0009_auto_20201218_0916'),
    ]

    operations = [
        migrations.CreateModel(
            name='AdminReg',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('club_name', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=20)),
                ('phone', models.CharField(max_length=20)),
            ],
        ),
    ]
