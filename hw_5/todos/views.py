from django.shortcuts import render, redirect
from .models import Todo
from .forms import StudentCreationForm

def get_index_page(request):
    todos = Todo.objects.all()
    form = StudentCreationForm()
    return render(request, 'index2.html', {'todos': todos, 'form': form})

def get_students_list(request):
    if request.method == 'GET':
        todos = Todo.objects.all()
        form = StudentCreationForm()
        return render(request, 'index2.html', {'todos': todos, 'form': form})

    elif request.method == 'POST':
        form = StudentCreationForm(request.POST)
        if form.is_valid():
            status_value = request.POST.get('status') == 'on'  # Преобразуем 'on' в True
            todo = Todo(
                title=form.cleaned_data.get('title'),
                description=form.cleaned_data.get('description'),
                due_date=form.cleaned_data.get('due_date'),
                status=status_value  # Исправленный статус
            )
            todo.save()
            return redirect(to='index_page')
        else:
            todos = Todo.objects.all()
            return render(request, 'index2.html', {'todos': todos, 'form': form})

def get_student(request, pk):
    try:
        w = Todo.objects.get(id=pk)
    except Todo.DoesNotExist:
        return redirect('todos_list_page')  # Перенаправление, если todo не найден
    return render(request, 'product-details.html', {'todo': w})

def delete_todo(request, pk):
    try:
        todo = Todo.objects.get(id=pk)
        todo.delete()
    except Todo.DoesNotExist:
        return redirect('todos_list_page')  # Перенаправление, если todo не найден
    return redirect('/todos/')

def edit_todo(request, pk):
    try:
        todos = Todo.objects.get(id=pk)
    except Todo.DoesNotExist:
        return redirect('todos_list_page')  # Перенаправление, если todo не найден

    if request.method == 'GET':
        form = StudentCreationForm(data={
            'title': todos.title,
            'description': todos.description,
            'due_date': todos.due_date,  # Исправлено с due_data на due_date
            'status': todos.status
        })
        return render(request, 'edit-todo.html', {'form': form, 'todo': todos})

    if request.method == 'POST':
        form = StudentCreationForm(request.POST)
        if form.is_valid():
            todos.title = form.cleaned_data.get('title')
            todos.description = form.cleaned_data.get('description')
            todos.due_date = form.cleaned_data.get('due_date')
            todos.status = request.POST.get('status') == 'on'  # Исправленный статус
            todos.save()
            return redirect('todos_list_page')
        else:
            return render(request, 'edit-todo.html', {'form': form, 'todo': todos, 'error': 'Something went wrong'})