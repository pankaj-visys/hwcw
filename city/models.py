from django.db import models
from django.contrib.auth import get_user_model

# Update-Start-PANKAJ.

# Create your models here.
class City(models.Model):
    #city_id = models.IntegerField(primary_key=True, unique=True)
    cityName = models.CharField(max_length=200, null=True, unique=True)

    def __str__(self):
        return self.cityName
    
class Grade(models.Model):
    #grade_id = models.IntegerField(primary_key=True, unique=True)
    gradeName = models.CharField(max_length=200, null=True)

    def __str__(self):
        return (self.gradeName)

class School(models.Model):
    #school_id = models.IntegerField(primary_key=True, unique=True)
    city = models.ForeignKey(City, on_delete = models.CASCADE)
    grade = models.ManyToManyField(Grade)
    schoolName = models.CharField(max_length=200, null=True)
    
    def __str__(self):
        return (self.schoolName)
    
class Book(models.Model):
    school = models.ManyToManyField(School, null=True)
    grade = models.ForeignKey(Grade, on_delete = models.CASCADE, null=True)
    writer = models.CharField(max_length=200, null=True)
    name = models.CharField(max_length = 100)
    price = models.IntegerField(default=0)
    stock = models.IntegerField(default=1)
    def __str__(self):
        return self.name
     
class OrderedBook(models.Model):
    book = models.ManyToManyField(Book, null=True)
    quantity = models.IntegerField()
    customer = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    bundle = models.BooleanField()
    
    def __str__(self):
	    return self.book.name

# Update-End-PANKAJ