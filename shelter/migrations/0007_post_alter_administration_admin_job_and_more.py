# Generated by Django 4.2.6 on 2024-04-03 18:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shelter', '0006_alter_administration_admin_job_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.CharField()),
                ('is_active', models.BooleanField(default=True)),
            ],
        ),
        migrations.AlterField(
            model_name='administration',
            name='admin_job',
            field=models.CharField(choices=[('DIR', 'director'), ('COORD', 'volunteer_coordinator'), ('VET', 'vet'), ('ADOPT', 'adoption_specialist'), ('SOC', 'socializer'), ('ACC', 'accountant'), ('HAND', 'handyman')], max_length=300),
        ),
        migrations.AlterField(
            model_name='animal',
            name='animal_sex',
            field=models.CharField(choices=[('FEMALE', 'Девочка'), ('MALE', 'Мальчик')], max_length=300),
        ),
    ]
