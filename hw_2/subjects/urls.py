from django.urls import path
from .views import get_courses_list, get_courses

urlpatterns = [
    path('', get_courses_list),
    path('<int:pk>/', get_courses)
]