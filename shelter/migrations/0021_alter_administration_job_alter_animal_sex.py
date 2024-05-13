# Generated by Django 4.2.6 on 2024-04-14 18:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shelter', '0020_alter_administration_job_alter_animal_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='administration',
            name='job',
            field=models.CharField(choices=[('Бухгалтер', 'Бухгалтер'), ('Социализатор', 'Социализатор'), ('Ветеринар', 'Ветеринар'), ('Разнорабочий', 'Разнорабочий'), ('Специалист по усыновлению', 'Специалист по усыновлению'), ('Директор', 'Директор'), ('Координатор волонеров', 'Координатор волонеров')], max_length=300),
        ),
        migrations.AlterField(
            model_name='animal',
            name='sex',
            field=models.CharField(choices=[('Девочка', 'Мальчик'), ('Девочка', 'Девочка')], max_length=300),
        ),
    ]