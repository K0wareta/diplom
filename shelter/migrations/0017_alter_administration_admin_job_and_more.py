# Generated by Django 4.2.6 on 2024-04-05 18:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shelter', '0016_alter_administration_admin_job_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='administration',
            name='admin_job',
            field=models.CharField(choices=[('SOC', 'socializer'), ('ADOPT', 'adoption_specialist'), ('DIR', 'director'), ('VET', 'vet'), ('HAND', 'handyman'), ('COORD', 'volunteer_coordinator'), ('ACC', 'accountant')], max_length=300),
        ),
        migrations.AlterField(
            model_name='animal',
            name='checkup_date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='animal',
            name='sex',
            field=models.CharField(choices=[('Мальчик', 'Мальчик'), ('Девочка', 'Девочка')], max_length=300),
        ),
    ]
