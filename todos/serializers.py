from .models import Cheese
from rest_framework import serializers

# Our TodoSerializer
class TodoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        # The model it will serialize
        model = Cheese
        # the fields that should be included in the serialized output
        fields = ['id', 'name', 'origin_country', 'type']