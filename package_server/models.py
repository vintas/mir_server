from django.db import models

# Create your models here.
class dependency(models.Model):
    name = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")

    def __str__(self):
        return self.name

class dependency_version(models.Model):
    dependency = models.ForeignKey(dependency, on_delete=models.CASCADE)
    version = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")

    # def __str__(self):
    #     return (self.dependency. + self.version)

class package(models.Model):
    name = models.CharField(max_length=200)
    version = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")

    def __str__(self):
        return self.name

class package_dependency(models.Model):
    package = models.ForeignKey(package, on_delete=models.CASCADE)
    dependency_version = models.ForeignKey(dependency_version, on_delete=models.CASCADE)
    pub_date = models.DateTimeField("date published")