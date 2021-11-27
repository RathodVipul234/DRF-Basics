from rest_framework import serializers
from .models import Student


# validator
def start_with_r(value):
    if value[0].lower() != 'r':
        raise serializers.ValidationError("Name should start with R")


class studentSerializers(serializers.Serializer):
    name = serializers.CharField(max_length=100, validators=[start_with_r])
    roll = serializers.IntegerField()
    city = serializers.CharField(max_length=100)

    def create(self, validated_data):
        return Student.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.city = validated_data.get('city', instance.city)
        instance.roll = validated_data.get('roll', instance.roll)
        instance.save()
        return instance

    def validate_roll(self, value):
        if value > 200:
            raise serializers.ValidationError('wrong roll no.')
        return value


# model serializer
# class studentModelSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Student
#         fields = '__all__'
#         read_only_fields = ['name', 'roll']
#         extra_kwargs = {
#             'name': {'read_only': True}
#         }
#         ''' by default create and update method include in model serializer'''
