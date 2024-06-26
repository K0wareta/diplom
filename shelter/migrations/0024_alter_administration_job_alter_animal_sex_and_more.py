# Generated by Django 4.2.6 on 2024-04-24 16:06

from django.db import migrations, models
import phone_field.models


class Migration(migrations.Migration):

    dependencies = [
        ('shelter', '0023_alter_administration_job_alter_animal_sex_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='administration',
            name='job',
            field=models.CharField(choices=[('Ветеринар', 'Ветеринар'), ('Директор', 'Директор'), ('Бухгалтер', 'Бухгалтер'), ('Координатор волонеров', 'Координатор волонеров'), ('Специалист по усыновлению', 'Специалист по усыновлению'), ('Социализатор', 'Социализатор'), ('Разнорабочий', 'Разнорабочий')], max_length=300),
        ),
        migrations.AlterField(
            model_name='animal',
            name='sex',
            field=models.CharField(choices=[('Мальчик', 'Мальчик'), ('Девочка', 'Девочка')], max_length=300),
        ),
        migrations.AlterField(
            model_name='animal',
            name='species',
            field=models.CharField(choices=[('Собака', 'Собака'), ('Кошка', 'Кошка')], max_length=300),
        ),
        migrations.AlterField(
            model_name='volunteer',
            name='phone',
            field=phone_field.models.PhoneField(help_text='Contact phone number', max_length=31),
        ),
    ]
