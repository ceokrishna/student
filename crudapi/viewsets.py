from rest_framework import viewsets
from crudapi.models import Student1
from crudapi import serializers

class StudentViewset(viewsets.ModelViewSet):
    queryset =Student1.objects.all()
    serializer_class = serializers.StudentSerializer

