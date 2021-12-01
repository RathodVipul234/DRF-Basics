from rest_framework import serializers
from .models import Student


# model serializer

class studentModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'

    '''
        # validation
        def validate_roll(self, value):
        if value > 200:
            raise serializers.ValidationError('wrong roll no.')
        return value
    '''
