# Generated by Django 3.2.2 on 2021-05-12 20:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='price',
            field=models.IntegerField(),
        ),
    ]
