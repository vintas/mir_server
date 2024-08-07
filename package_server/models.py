from django.db import models
from django.contrib.auth.models import User
from .validators import validate_semver

class Library(models.Model):
    name = models.CharField(max_length=100)
    version = models.CharField(max_length=50, validators=[validate_semver])
    file = models.FileField(upload_to='library_files/', blank=False, null=False)
    dependencies = models.ManyToManyField('self', symmetrical=False, blank=True, related_name='dependent_libraries')

    def __str__(self):
        return f"{self.name} ({self.version})"

class Package(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    version = models.CharField(max_length=50, validators=[validate_semver])
    description = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    libraries = models.ManyToManyField(Library, blank=True)
    file = models.FileField(upload_to='package_files/', blank=False, null=False)
    dependencies = models.ManyToManyField('self', symmetrical=False, blank=True, related_name='dependent_packages')
    setup_script = models.FileField(upload_to='shell_scripts/', blank=True, null=True)

    def __str__(self):
        return f"{self.name} ({self.version})"
