from django.db import models


class Volunteer(models.Model):  # Привести в порядок
    name = models.CharField(max_length=300)
    phone = models.CharField(max_length=300)
    rights = models.CharField(max_length=300)
    regime = models.CharField(max_length=300)


SPECIES = {
    ('Кошка', 'Кошка'),
    ('Собака', 'Собака')
}

SEX = {
    ('Девочка', 'Девочка'),
    ('Мальчик', 'Мальчик')
}


class Animal(models.Model):
    photo = models.ImageField(blank=True, upload_to='images/')
    species = models.CharField(choices=SPECIES, max_length=300)
    name = models.CharField(max_length=300)
    age = models.IntegerField()
    weight = models.IntegerField()
    sex = models.CharField(choices=SEX, max_length=300)
    admission_date = models.DateField()
    health_status = models.CharField(max_length=300)
    medical_history = models.CharField(max_length=300)
    checkup_date = models.DateField()
    behaviour = models.CharField(max_length=300)
    status = models.CharField(max_length=300)
    notes = models.CharField(max_length=300)

    def __str__(self):
        return self.name


JOB = {
    ('Директор', 'Директор'),
    ('Бухгалтер', 'Бухгалтер'),
    ('Социализатор', 'Социализатор'),
    ('Ветеринар', 'Ветеринар'),
    ('Координатор волонеров', 'Координатор волонеров'),
    ('Специалист по усыновлению', 'Специалист по усыновлению'),
    ('Разнорабочий', 'Разнорабочий')
}


class Administration(models.Model):
    name = models.CharField(max_length=300)
    job = models.CharField(choices=JOB, max_length=300)
    salary = models.IntegerField()

    def __str__(self):
        return self.name


class Resources(models.Model):
    money = models.FloatField()
    meds = models.FloatField()
    cat_food = models.FloatField()
    dog_food = models.FloatField()

    def __str__(self):
        return 'resource'
