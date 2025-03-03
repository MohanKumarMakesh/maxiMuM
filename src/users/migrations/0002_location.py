# Generated by Django 5.1.6 on 2025-03-03 07:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address_1', models.CharField(max_length=255)),
                ('address_2', models.CharField(blank=True, max_length=255)),
                ('city', models.CharField(max_length=100)),
            ],
        ),
    ]
