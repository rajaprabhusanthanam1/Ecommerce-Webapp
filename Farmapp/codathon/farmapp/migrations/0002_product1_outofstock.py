# Generated by Django 4.2.5 on 2023-10-03 15:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('farmapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product1',
            name='outofstock',
            field=models.BooleanField(default=False),
        ),
    ]
