from rest_framework import serializers

from .models import Household, DogOwner, Dog

# Not really sure how to do this with inheritance - settling for just
# serializing as though there wasn't any inheritance, just to get me over this
# hump.
class DogOwnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = DogOwner
        fields = ('id', 'name')

class DogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dog
        fields = ('id', 'name', 'age', 'weight', 'play_style')

class HouseholdSerializer(serializers.ModelSerializer):
    dogOwners = DogOwnerSerializer(many=True)
    dogs = DogSerializer(many=True)

    class Meta:
        model = Household
        fields = ('id', 'address', 'city', 'state', 'zip_code', 'fenced_yard', 'dogOwners', 'dogs')
