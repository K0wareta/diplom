from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound, HttpResponseForbidden
from shelter.models import Animal, Resources, Administration, Volunteer
from .forms import AnimalForm
from django.contrib.auth.decorators import user_passes_test


def is_shelter_member(user):
    return user.groups.filter(name='Shelter members').exists()

def access_denied_view(request):
    return HttpResponseForbidden('У вас нет доступа к этой странице.')

@user_passes_test(is_shelter_member)
def animals(request):
    animals = Animal.objects.all()
    return render(request, "animals.html", {"animals": animals})


def contacts(request):
    return render(request, "contacts.html")


@user_passes_test(is_shelter_member)
def panel(request):
    workers = Administration.objects.all()
    resources = Resources.objects.first()
    animals = Animal.objects.all()
    total_animals = animals.count()

    dog_dict = {
        2: 40,
        5: 90,
        10: 150,
        20: 240,
        30: 360,
        40: 440,
        50: 510
    }

    cat_dict = {
        2: 40,
        3: 45,
        4: 60,
        5: 75,
        6: 80,
        8: 90,
        10: 120
    }

    total_dog_food = 0
    total_cat_food = 0

    for animal in animals:
        if animal.species == "Собака":
            for w, food_amount in dog_dict.items():
                if animal.weight > 50:
                    total_dog_food += 510
                    break
                if animal.weight <= w:
                    total_dog_food += food_amount
                    break
        elif animal.species == "Кошка":
            for w, food_amount in cat_dict.items():
                if animal.weight > 10:
                    total_cat_food += 120
                    break
                elif animal.weight <= w:
                    total_cat_food += food_amount
                    break

    salary_arr = []
    for i in workers:
        salary_arr.append(i.salary)

    money = resources.money // (sum(salary_arr) / 30)
    meds = resources.meds // (total_animals * 10)
    cat_food = resources.cat_food // (total_cat_food / 1000)
    dog_food = resources.dog_food // (total_dog_food / 1000)
    return render(request, "panel.html",
                  {"resources": resources, "money": money, "meds": meds, "cat_food": cat_food, "dog_food": dog_food})


def index(request):
    animals = Animal.objects.all()
    return render(request, "index.html", {"animals": animals})


@user_passes_test(is_shelter_member)
def create_animal(request):
    if request.method == "POST":
        form = AnimalForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/")
        else:
            raise Exception('Data')
    else:
        form = AnimalForm()
    return render(request, 'animals.html', {'form': form})


@user_passes_test(is_shelter_member)
def edit_animal(request, id):
    try:
        animal = Animal.objects.get(id=id)

        if request.method == "POST":
            # Получение необходимых полей из формы
            photo = request.FILES.get("photo")
            species = request.POST.get("species")
            name = request.POST.get("name")
            age = request.POST.get("age")
            weight = request.POST.get("weight")
            sex = request.POST.get("sex")
            admission_date = request.POST.get("admission_date")
            health_status = request.POST.get("health_status")
            medical_history = request.POST.get("medical_history")
            checkup_date = request.POST.get("checkup_date")
            behaviour = request.POST.get("behaviour")
            status = request.POST.get("status")
            notes = request.POST.get("notes")

            # Обновление соответствующих полей объекта "animal"
            if photo:
                animal.photo = photo
            if species:
                animal.species = species
            if name:
                animal.name = name
            if age:
                animal.age = age
            if weight:
                animal.weight = weight
            if sex:
                animal.sex = sex
            if admission_date:
                animal.admission_date = admission_date
            if health_status:
                animal.health_status = health_status
            if medical_history:
                animal.medical_history = medical_history
            if checkup_date:
                animal.checkup_date = checkup_date
            if behaviour:
                animal.behaviour = behaviour
            if status:
                animal.status = status
            if notes:
                animal.notes = notes
            animal.save()

            # Перенаправление на главную страницу
            return HttpResponseRedirect("/")
        else:
            form = AnimalForm(instance=animal)
        return render(request, "edit_animal.html", {"form": form})
    except Animal.DoesNotExist:
        return HttpResponseNotFound("<h2>Animal not found</h2>")


@user_passes_test(is_shelter_member)
def delete_animal(request, id):
    try:
        animal = Animal.objects.get(id=id)
        animal.delete()
        return HttpResponseRedirect("/")
    except Animal.DoesNotExist:
        return HttpResponseNotFound("<h2>Animal not found</h2>")


def volunteers(request):
    volunteers = Volunteer.objects.all()
    return render(request, 'volunteers.html', {"volunteers": volunteers})
