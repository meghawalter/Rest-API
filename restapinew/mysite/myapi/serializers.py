from rest_framework import serializers
from myapi.models import Student

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        # fields = ('name', 'rollno')
        fields= '__all__'
