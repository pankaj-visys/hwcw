from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Book, City, Grade, School


admin.site.register(Grade)


class CityAdmin(admin.ModelAdmin):
    model = City
    list_display = ['pk', 'cityName']

admin.site.register(City, CityAdmin)

class SchoolAdmin(admin.ModelAdmin):
    model = School
    list_display = ['pk', 'city', 'schoolName']

admin.site.register(School, SchoolAdmin)

class BookAdmin(admin.ModelAdmin):
    model = Book
    list_display = ['pk', 'name']

admin.site.register(Book, BookAdmin)