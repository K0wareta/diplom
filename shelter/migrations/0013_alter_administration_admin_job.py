# Generated by Django 4.2.6 on 2024-04-05 16:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shelter', '0012_remove_animal_type_animal_species_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='administration',
            name='admin_job',
            field=models.CharField(choices=[('DIR', 'director'), ('VET', 'vet'), ('HAND', 'handyman'), ('ACC', 'accountant'), ('COORD', 'volunteer_coordinator'), ('ADOPT', 'adoption_specialist'), ('SOC', 'socializer')], max_length=300),
        ),
    ]