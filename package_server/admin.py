from django.contrib import admin

# Register your models here.
from .models import dependency,dependency_version,package,package_dependency

admin.site.register(dependency)
admin.site.register(dependency_version)
admin.site.register(package)
admin.site.register(package_dependency)
