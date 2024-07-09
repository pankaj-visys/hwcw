from django.shortcuts import render
from rest_framework import generics
from .models import Book, City, Grade, School
from .serializers import BookSerializer, CitySerializer, GradeSerializer, SchoolSerializer
# Create your views here.
# api/views.py

class BookList(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookDetail(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class CityList(generics.ListAPIView):
    queryset = City.objects.all()
    serializer_class = CitySerializer

class SchoolList(generics.ListAPIView):
    queryset = School.objects.all()
    serializer_class = SchoolSerializer

class GradeList(generics.ListAPIView):
    queryset = Grade.objects.all()
    serializer_class = GradeSerializer


# Create your views here.
def city_list(request):
    cities = City.objects.all()
    context = {'cities': cities}
    return render(request, 'city_list.html', context)

def school_list(request):
    #Get selected city object
    selectedCity = request.GET.get('city')
    print(selectedCity)
    selectedCityObject = City.objects.filter(cityName=selectedCity)[0].pk
    schools = School.objects.filter(city=selectedCityObject)
    print(schools[0])
    context = {'schools': schools}
    return render(request, 'school_list.html', context)

def grade_list(request):
    selectedSchool = request.GET.get('school')
    grades = School.objects.filter(schoolName=selectedSchool)[0].grade.all()
    context = {'grades': grades}
    return render(request, 'grade_list.html', context)


def all_list(request):
    #Get all cities
    cities = City.objects.all()
    
    #Get selected city object
    selectedCity = cities[0]
    selectedCityObject = City.objects.filter(cityName=selectedCity)[0].pk
    schools = School.objects.filter(city=selectedCityObject)

    #Get selected grade object
    selectedSchool = schools[0]
    grades = School.objects.filter(schoolName=selectedSchool)[0].grade.all()
 
    context = {'cities': cities,
               'schools': schools,
               'grades': grades
               }

    return render(request, 'all_list.html', context)


def click_all_list(request):
    #Get all cities
    cities = City.objects.all()
    
    #Get selected city object
    selectedCity = cities[0]
    selectedCityObject = City.objects.filter(cityName=selectedCity)[0].pk
    schools = School.objects.filter(city=selectedCityObject)

    #Get selected grade object
    selectedSchool = schools[0]
    grades = School.objects.filter(schoolName=selectedSchool)[0].grade.all()
 
    context = {'cities': cities,
               'schools': schools,
               'grades': grades
               }

    return render(request, 'click_all_list.html', context)


def updateSchoolGradeGroup(request):
    #Get selected city object
    selectedCity = request.GET.get('cityBoxName')
    print("This is selected city")
    print(selectedCity)

    selectedCityObject = City.objects.filter(cityName=selectedCity)[0].pk
    schools = School.objects.filter(city=selectedCityObject)
    
    if any(schools):
        print(schools[0])

        selectedSchool = schools[0]
        grades = School.objects.filter(schoolName=selectedSchool)[0].grade.all()
        print(grades[0])
    
    else:
        grades=[]
    

    context = {'schools': schools,
               'grades': grades}
    return render(request, 'updateSchoolGradeGroup.html', context)


def updateGradeBox(request):
    selectedSchool = request.GET.get('schoolBoxName')
    print("This is updateGradeBox")
    print(selectedSchool)

    grades = School.objects.filter(schoolName=selectedSchool)[0].grade.all()
    context = {'grades': grades}
    return render(request, 'updateGradeBox.html', context)


def book_List(request):
    selectedCity = request.GET.get('cityBoxName')
    selectedSchool = request.GET.get('schoolBoxName')
    selectedGrade = request.GET.get('gradeBoxName')

    if selectedSchool=="":
        books=[]
        counter=1
        print("Selected school is NULL")
    else:
        selectedSchoolObject = School.objects.filter(schoolName=selectedSchool)[0].pk
        selectedGradeObject = Grade.objects.filter(gradeName=selectedGrade)[0].pk

        books = Book.objects.filter(school=selectedSchoolObject)
        books = books.filter(grade=selectedGradeObject)

        counter=[]
        for i in range(len(books)):
            counter.append(i)
        print(counter)

 
    context = {'city': selectedCity,
               'school': selectedSchool,
               'grade': selectedGrade,
               'books': books,
               'counte': 12,
               }

    return render(request, 'book_List.html', context)

def decrement(request):
    quantity = int(request.GET.get('quantity'))
    print("Old quantity decrement = ",quantity)

    if (quantity==0):
        newQuantity=quantity
    else: 
        newQuantity=quantity-1
    print("New quantity decrement = ",newQuantity)
    context = {'newQuantity': newQuantity,
               }
    return render(request, 'decrement.html', context)

def increment(request):
    quantity = int(request.GET.get('quantity'))
    print("Old quantity increment = ",quantity)

    newQuantity=quantity+1

    print("New quantity increment = ",newQuantity)
    
    context = {'newQuantity': newQuantity,
               }
    return render(request, 'decrement.html', context)