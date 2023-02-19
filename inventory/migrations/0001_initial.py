# Generated by Django 4.1.7 on 2023-02-19 01:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Inventory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('quantity', models.IntegerField()),
                ('department', models.CharField(max_length=100)),
                ('image', models.CharField(max_length=250)),
                ('details', models.CharField(max_length=250)),
                ('location', models.CharField(max_length=20)),
            ],
        ),
    ]