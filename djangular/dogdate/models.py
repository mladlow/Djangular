from django.db import models

# Households represent groups of owners and dogs. They have an address, and
# the option to have a fenced yard, which could be useful for scheduling non
# dogpark playdates.
class Household(models.Model):
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=25)
    state = models.CharField(max_length=2)
    zip_code = models.IntegerField()
    fenced_yard = models.BooleanField()

# The HouseholdResident class is a superclass for dogs and owners, since the
# name and (TODO) profile picture are common items between the two.
# In this case, I want to just hold common information, so this should be an
# abstract base class (https://docs.djangoproject.com/en/1.8/topics/db/models/#abstract-base-classes)
class HouseholdResident(models.Model):
    household = models.ForeignKey(Household)
    name = models.CharField(max_length=50)

    class Meta:
        abstract = True
    # TODO: profile_picture
    #profile_picture = models.ImageField()

# DogOwners can have a schedule representing when they are typically available
# to participate in a doggy playdate.
class DogOwner(HouseholdResident):
    # Actually implementation of Schedule is not in the MVP
    schedule = models.TextField()

# Dogs have age, weight (representing general size), and can have a blurb 
# about their play style.
class Dog(HouseholdResident):
    age = models.IntegerField()
    weight = models.IntegerField()
    play_style = models.TextField()
