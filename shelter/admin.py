from django.contrib import admin

from .models import Animal, Resources, Administration, Volunteer

admin.site.register(Animal)
admin.site.register(Resources)
admin.site.register(Administration)
admin.site.register(Volunteer)