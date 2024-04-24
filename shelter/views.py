from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound
from shelter.models import Animal, Resources, Administration, Volunteer
from .forms import AnimalForm


def animals(request):
    animals = Animal.objects.all()
    return render(request, "animals.html", {"animals": animals})


def contacts(request):
    return render(request, "contacts.html")


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


def edit_animal(request, id):
    try:
        animal = Animal.objects.get(id=id)

        if request.method == "POST":
            form = AnimalForm(request.POST, request.FILES, instance=animal)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect("/")
        else:
            form = AnimalForm(instance=animal)
        return render(request, "edit_animal.html", {"form": form})
    except Animal.DoesNotExist:
        return HttpResponseNotFound("<h2>Animal not found</h2>")


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