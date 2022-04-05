from django.db import models


# Create your models here.

class Person(models.Model):
    firstName = models.CharField(max_length=60)
    lastName = models.CharField(max_length=60)
    school = models.CharField(max_length=60)
    major = models.CharField(max_length=60)
    religion = models.CharField(max_length=60)

    def __str__(self):
        return self.firstName


class Hobby(models.Model):
    name = models.CharField(max_length=60)

    pid = models.ForeignKey(Person, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
