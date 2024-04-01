# Generated by Django 4.2.6 on 2024-04-01 18:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shelter', '0005_auto_20240401_2018'),
    ]

    operations = [
        migrations.AlterField(
            model_name='administration',
            name='admin_job',
            field=models.CharField(choices=[('SOC', 'socializer'), ('HAND', 'handyman'), ('VET', 'vet'), ('ACC', 'accountant'), ('DIR', 'director'), ('ADOPT', 'adoption_specialist'), ('COORD', 'volunteer_coordinator')], max_length=300),
        ),
        migrations.AlterField(
            model_name='animal',
            name='animal_sex',
            field=models.CharField(choices=[('MALE', 'Мальчик'), ('FEMALE', 'Девочка')], max_length=300),
        ),
        migrations.AlterField(
            model_name='animal',
            name='animal_type',
            field=models.CharField(choices=[('CAT', 'Кошка'), ('DOG', 'Собака')], max_length=300),
        ),
    ]
