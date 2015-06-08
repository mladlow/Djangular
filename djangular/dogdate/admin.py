from django.contrib import admin
from dogdate.models import Household, DogOwner, Dog

class DogOwnerInline(admin.StackedInline):
    model = DogOwner
    extra = 2
    # I decided not to try for the schedule in the MVP, so it's not in the
    # fieldsets - I'm not really sure how I want to represent it yet.
    fieldsets = [ (None, {'fields': ['name']}) ]

class DogInline(admin.StackedInline):
    model = Dog
    extra = 1

class HouseholdAdmin(admin.ModelAdmin):
    inlines = [DogOwnerInline, DogInline] 
    list_display = ('address', 'city', 'state', 'zip_code')

admin.site.register(Household, HouseholdAdmin)
