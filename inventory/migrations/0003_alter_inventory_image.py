# Generated by Django 4.1.7 on 2023-02-22 01:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0002_alter_inventory_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inventory',
            name='image',
            field=models.ImageField(upload_to='images'),
        ),
    ]
