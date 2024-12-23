from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm

# Create your views here.
def index(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()  # Save the form data to the database
            return redirect('index')  # Redirect to the same page after submission
    else:
        form = TaskForm()
    
    tasks = Task.objects.all()
    context = {'tasks': tasks, 'form': form}
    return render(request, 'list.html', context)
