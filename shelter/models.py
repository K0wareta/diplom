from django.db import models


class Volunteer(models.Model):  # Привести в порядок
    volunteer_name = models.CharField(max_length=300)
    volunteer_phone = models.CharField(max_length=300)
    volunteer_rights = models.CharField(max_length=300)
    volunteer_regime = models.CharField(max_length=300)


ANIMAL_TYPES = {
    ('CAT', 'Кошка'),
    ('DOG', 'Собака')
}

ANIMAL_SEX = {
    ('FEMALE', 'Девочка'),
    ('MALE', 'Мальчик')
}


class Animal(models.Model):  # Привести в порядок
    animal_photo = models.ImageField(blank=True)
    animal_type = models.CharField(choices=ANIMAL_TYPES, max_length=300)
    animal_name = models.CharField(max_length=300)
    animal_age = models.IntegerField()
    animal_weight = models.IntegerField()
    animal_sex = models.CharField(choices=ANIMAL_SEX, max_length=300)
    animal_admission_date = models.DateField()
    animal_health_status = models.CharField(max_length=300)
    animal_medical_history = models.CharField(max_length=300)
    animal_checkup_date = models.DateField()
    animal_behaviour = models.CharField(max_length=300)
    animal_status = models.CharField(max_length=300)
    animal_notes = models.CharField(max_length=300)

    def __str__(self):
         return self.animal_name

JOB = {
    ('DIR', 'director'),  # босс
    ('ACC', 'accountant'),  # бухгалтерия, ивенты
    ('SOC', 'socializer'),  # социализация животных
    ('VET', 'vet'),  # ветеринар
    ('COORD', 'volunteer_coordinator'),  # координатор волонтеров
    ('ADOPT', 'adoption_specialist'),  # специалист по усыновлению + PR
    ('HAND', 'handyman')  # разнорабочий
}


class Administration(models.Model):
    admin_name = models.CharField(max_length=300)
    admin_job = models.CharField(choices=JOB, max_length=300)
    admin_salary = models.IntegerField()


class Resources(models.Model):
    resources_money = models.IntegerField()
    resources_meds = models.IntegerField()
    resources_cat_food = models.IntegerField()
    resources_dog_food = models.IntegerField()
