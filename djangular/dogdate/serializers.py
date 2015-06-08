from rest_framework import serializers

from .models import Household, DogOwner, Dog

class Household(serializers.ModelSerializer):
    class Meta:
        model = Household
        fields = ('id', 'address', 'city', 'state', 'zip_code', 'fenced_yard')

# Not really sure how to do this with inheritance.
#class DogOwnerSerializer(serializers.ModelSerializer):
#    class Meta:
