from rest_framework import serializers
from crudapi.models import Student1

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Student1
        fields='__all__'