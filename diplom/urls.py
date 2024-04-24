"""
URL configuration for diplom project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
from shelter import views
from django.conf.urls.static import static
from django.conf import settings
from shelter.views import *


urlpatterns = [
    path("", views.index),
    path("animals/create_animal/", views.create_animal),
    path("animals/edit_animal/<int:id>/", views.edit_animal),
    path("animals/delete_animal/<int:id>/", views.delete_animal),
    path('admin/', admin.site.urls),
    path("animals/", views.animals),
    path("contacts/", views.contacts),
    path("panel/", views.panel),
    path("volunteers/", views.volunteers)
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)