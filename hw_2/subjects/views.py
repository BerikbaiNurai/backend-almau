from django.shortcuts import render
from .models import Courses

def get_courses_list(request):
    courses = Courses.objects.all()
    return  render(request, 'index.html', {'courses': courses})

def get_courses(request, pk):
    course = Courses.objects.get(id=pk)
    return render(request, 'course-details.html', {'course': course})
