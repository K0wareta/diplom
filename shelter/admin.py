from django.contrib import admin

from .models import Animal, Resources, Administration

admin.site.register(Animal)
admin.site.register(Resources)
admin.site.register(Administration)