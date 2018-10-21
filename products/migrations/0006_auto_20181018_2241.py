# Generated by Django 2.1.1 on 2018-10-18 17:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0011_auto_20181018_2241'),
        ('products', '0005_product_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='Manufacturer',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='mainapp.Manufacturer'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='country',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
    ]
