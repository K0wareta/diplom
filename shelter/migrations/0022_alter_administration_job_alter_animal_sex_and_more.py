# Generated by Django 4.2.6 on 2024-04-24 11:39

from django.db import migrations, models
import phone_field.models


class Migration(migrations.Migration):

    dependencies = [
        ('shelter', '0021_alter_administration_job_alter_animal_sex'),
    ]

    operations = [
        migrations.AlterField(
            model_name='administration',
            name='job',
            field=models.CharField(choices=[('Координатор волонеров', 'Координатор волонеров'), ('Социализатор', 'Социализатор'), ('Бухгалтер', 'Бухгалтер'), ('Разнорабочий', 'Разнорабочий'), ('Ветеринар', 'Ветеринар'), ('Специалист по усыновлению', 'Специалист по усыновлению'), ('Директор', 'Директор')], max_length=300),
        ),
        migrations.AlterField(
            model_name='animal',
            name='sex',
            field=models.CharField(choices=[('Мальчик', 'Мальчик'), ('Девочка', 'Девочка')], max_length=300),
        ),
        migrations.AlterField(
            model_name='volunteer',
            name='phone',
            field=phone_field.models.PhoneField(blank=True, help_text='Contact phone number', max_length=31),
        ),
    ]
