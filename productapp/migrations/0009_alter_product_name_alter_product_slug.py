# Generated by Django 4.2.1 on 2023-05-28 14:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productapp', '0008_order_total'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(max_length=60, unique=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='slug',
            field=models.SlugField(max_length=60, unique=True),
        ),
    ]
