from rest_framework import serializers
from mainapp.models import *

class bookserializer(serializers.ModelSerializer):
    class Meta:
        model=Book
        fields='__all__'

