from rest_framework import serializers
from .models import Student


# model serializer

class studentModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'
