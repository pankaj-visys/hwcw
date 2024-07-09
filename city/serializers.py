from rest_framework import serializers
from .models import Book, City, Grade, School

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ('school', 'grade', 'writer', 'name', 'price')

class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = ('cityName',)

class GradeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Grade
        fields = ('gradeName',)

class SchoolSerializer(serializers.ModelSerializer):
    class Meta:
        model = School
        fields = ('city', 'grade', 'schoolName',)