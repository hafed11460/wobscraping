# Generated by Django 3.2 on 2022-03-24 08:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fontionbooks',
            name='currency',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='currency'),
        ),
        migrations.AlterField(
            model_name='fontionbooks',
            name='sku',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='currency'),
        ),
    ]
