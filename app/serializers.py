from rest_framework import serializers
from .models import Student 

# Create your models here.
class StudentSerializer(serializers.Serializer):
    class Meta:
        model = Student
        fields = '__all__'        
    
    def create(self, validated_data):
        return Student.objects.create(**validated_data)