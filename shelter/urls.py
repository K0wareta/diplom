from django.urls import path

from shelter import views

urlpatterns = [
    path("", views.index, name="index"),
    path("animals/", views.animals, name="animals"),
    path("contacts/", views.contacts, name="contacts"),
]