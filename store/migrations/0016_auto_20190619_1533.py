# Generated by Django 2.2.2 on 2019-06-19 07:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0015_auto_20190619_1532'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='productCode',
            field=models.CharField(max_length=30, unique=True),
        ),
    ]