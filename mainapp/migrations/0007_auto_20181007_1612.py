# Generated by Django 2.1.1 on 2018-10-07 11:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0006_kettle_manufacturer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='armchair',
            name='country',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='kettle',
            name='country',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='lamp',
            name='country',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='table',
            name='country',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
    ]
