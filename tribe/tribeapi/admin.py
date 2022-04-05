from django.contrib import admin

# Register your models here.
from .models import Hobby, Person

admin.site.register(Hobby)
admin.site.register(Person)
