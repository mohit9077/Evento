# Generated by Django 3.0.5 on 2020-12-18 03:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_auto_20201218_0912'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userreg',
            name='branch',
            field=models.CharField(choices=[('CSE', 'Computer Science'), ('ISE', 'Information Science'), ('ECE', 'Electronics')], default='', max_length=3, verbose_name='subject'),
        ),
    ]
