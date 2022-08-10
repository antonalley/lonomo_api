from django.db import models
from django.contrib.auth.models import User


class InterestCategory(models.Model):
    name = models.CharField(max_length=120)

    def __str__(self):
        return self.name

class Interest(models.Model):
    name = models.CharField(max_length=120)
    required = models.BooleanField(default=False)
    category = models.ManyToManyField(InterestCategory, blank=True, null=True)
    open_response = models.BooleanField(default=False)  # If The interest requires text input

    def __str__(self):
        return self.name
class RelatedInterest(models.Model):
    interest_one = models.ForeignKey(Interest, on_delete=models.CASCADE, related_name="interest_one")
    interest_two = models.ForeignKey(Interest, on_delete=models.CASCADE, related_name="interest_two")
    strength = models.IntegerField()  # Scale of 1 - 10

    def __str__(self):
        return self.interest_one.name + " - " + self.interest_two.name


class PersonInterest(models.Model):
    interest = models.ForeignKey(Interest, on_delete=models.CASCADE)
    person = models.ForeignKey(User, on_delete=models.CASCADE)
    detail = models.CharField(max_length=120, blank=True, null=True)  # Used when Interest.open_response is true for user response

    def __str__(self):
        return self.person.username + ' -> '+ self.interest.name


