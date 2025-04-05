from django.urls import path
from .views import get_students_list, get_student, delete_todo, delete_from_todo_list, add_to_todo_list

urlpatterns = [
    path('', get_students_list, name='todos_list'),
    path('<int:pk>/', get_student, name='todo_details'),
    path('<int:pk>/delete/', delete_todo),
    path('todos/<int:pk>/add/', add_to_todo_list, name='add_to_todo_list'),
    path('todos/<int:pk>/delete/', delete_from_todo_list, name='delete_from_todo_list'),
]
