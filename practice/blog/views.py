from django.shortcuts import render, redirect
from .models import Blog
from .forms import StudentCreationForm

def get_students_list(request):
    if request.method == 'GET':
        blogs = Blog.objects.all()
        form = StudentCreationForm()
        print(blogs)
        return render(request, 'index2.html', {'blogs': blogs, 'form': form})
    elif request.method == 'POST':
        print(request.POST)
        form = StudentCreationForm(data=request.POST)
        print(form.is_valid())
        if form.is_valid():
            print('okokoko')
            form.save()
            return redirect('/blog/')
        else:
            blogs = Blog.objects.all()
            return render(request, 'index2.html', {'blogs': blogs, 'form': form})

def get_student(request, pk):
    w = Blog.objects.get(id=pk)
    return render(request, 'product-details.html', {'blog': w})

def delete_blog(request, pk):
    try:
        blog = Blog.objects.get(id=pk)
        blog.delete()
        return redirect('/blog/')
    except Blog.DoesNotExist as e:
        blogs = Blog.objects.all()
        form = StudentCreationForm()
        return render(request, 'index2.html', {'blogs': blogs, 'form': form, 'error': 'Blog does not exist'})
