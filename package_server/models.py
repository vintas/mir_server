from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Library(models.Model):
    name = models.CharField(max_length=100)
    version = models.CharField(max_length=50)
    file = models.FileField(upload_to='library_files/', blank=True, null=True)

    def __str__(self):
        return f"{self.name} ({self.version})"

class Package(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField()
    version = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    libraries = models.ManyToManyField(Library, blank=True)
    file = models.FileField(upload_to='package_files/', blank=True, null=True)

    def __str__(self):
        return f"{self.name} ({self.version})"