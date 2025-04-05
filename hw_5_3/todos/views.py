from django.shortcuts import render, redirect
from .models import Todo
from .forms import StudentCreationForm

def get_students_list(request):
    if request.method == 'GET':
        todos = Todo.objects.filter(user_id=request.user.id)
        form = StudentCreationForm()
        return render(request, 'index2.html', {'todos': todos, 'form': form})
    elif request.method == 'POST':
        form = StudentCreationForm(request.POST)
        if form.is_valid():
            form.save(commit=False)
            title = form.data.get('title')
            description = form.data.get('description')
            due_date = form.data.get('due_date')
            status = form.data.get('status') == 'on'

            todo = Todo(title=title, description=description, due_date=due_date, status=status, user_id=request.user.id)
            todo.save()
            return redirect('/todos/')
        else:
            todos = Todo.objects.all()
            return render(request, 'index2.html', {'todos': todos, 'form': form})


def get_student(request, pk):
    w = Todo.objects.get(id=pk)
    return render(request, 'product-details.html', {'todo': w})

def delete_todo(request, pk):
    try:
        todo = Todo.objects.get(id=pk)
        todo.delete()
        return redirect('/todos/')
    except Todo.DoesNotExist as e:
        todos = Todo.objects.all()
        form = StudentCreationForm()
        return render(request, 'index2.html', {'todos': todos, 'form': form, 'error': 'Todo does not exist'})

def add_to_todo_list(request, pk):
    if request.user and request.user.is_authenticated:
        try:
            todo = Todo.objects.get(id=pk)
            # Проверяем, если эта задача уже была добавлена пользователем (например, через связь Many-to-Many)
            if request.user.todo_set.filter(id=todo.id).exists():
                return redirect(to='todos_list')  # Если задача уже есть, не добавляем снова
            # Добавляем задачу к пользователю
            request.user.todo_set.add(todo)  # Важно, чтобы было Many-to-Many отношение
            return redirect(to='todos_list')
        except Todo.DoesNotExist as e:
            return redirect(to='todos_list')  # Если задача не найдена
    else:
        return redirect('/auth/login/')  # Если пользователь не аутентифицирован

# Функция для удаления задачи из списка пользователя
def delete_from_todo_list(request, pk):
    if request.user and request.user.is_authenticated:
        try:
            todo = Todo.objects.get(id=pk)
            if request.user.todo_set.filter(id=todo.id).exists():
                request.user.todo_set.remove(todo)  # Удаляем задачу из списка пользователя
            return redirect(to='todos_list')
        except Todo.DoesNotExist as e:
            return redirect(to='todos_list')  # Если задача не найдена
    else:
        return redirect('/auth/login/')  # Если пользователь не аутентифицирован
