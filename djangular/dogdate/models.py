from django.db import models

# Create your models here.
class Household(models.Model):
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=25)
    state = models.CharField(max_length=2)
    zip_code = models.IntegerField()
    fenced_yard = models.BooleanField()

class HouseholdResident(models.Model):
    household = models.ForeignKey(Household)
    name = models.CharField(max_length=50)
    # TODO: profile_picture
    #profile_picture = models.ImageField()

class DogOwner(HouseholdResident):
    # Actually implementation of Schedule is not in the MVP
    schedule = models.TextField()

class Dog(HouseholdResident):
    weight = models.IntegerField()
    play_style = models.TextField()
