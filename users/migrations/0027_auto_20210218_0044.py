# Generated by Django 2.1.7 on 2021-02-17 19:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0026_auto_20210218_0004'),
    ]

    operations = [
        migrations.AlterField(
            model_name='adminreg',
            name='password1',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='adminreg',
            name='password2',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='userreg',
            name='password1',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='userreg',
            name='password2',
            field=models.CharField(max_length=10),
        ),
    ]
