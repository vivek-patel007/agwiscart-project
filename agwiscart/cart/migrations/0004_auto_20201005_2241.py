# Generated by Django 3.1.1 on 2020-10-06 05:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0003_auto_20201005_2139'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart_item',
            name='quantity',
            field=models.IntegerField(default=1),
        ),
    ]