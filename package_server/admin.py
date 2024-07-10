from django.contrib import admin

# Register your models here.
from .models import Package,Library

admin.site.register(Package)
admin.site.register(Library)
