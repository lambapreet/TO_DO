from django.shortcuts import render, redirect, get_object_or_404
from .models import Task
from .forms import TaskForm

# Index view for displaying and adding tasks
def index(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()  # Save the form data to the database
            return redirect('index')  # Redirect to the same page after submission
    else:
        form = TaskForm()  # Instantiate an empty form
    
    tasks = Task.objects.all()  # Fetch all tasks from the database
    context = {'tasks': tasks, 'form': form}
    return render(request, 'list.html', context)  # Render the template with tasks and the form

# Update view for modifying an existing task
def update(request, pk):
    # Get the task object or raise a 404 error if it doesn't exist
    task = get_object_or_404(Task, id=pk)

    # Check if the request is a POST (form submission)
    if request.method == 'POST':
        # Populate the form with the submitted data and the existing task instance
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()  # Save the updated task
            return redirect('index')  # Redirect to the index page or another appropriate view
    else:
        # If not a POST request, populate the form with the existing task data
        form = TaskForm(instance=task)

    # Render the template with the form
    return render(request, 'update_task.html', {'form': form})


def delete(request, pk):
    # Get the task object or raise a 404 error if it doesn't exist
    item = get_object_or_404(Task, id=pk)

    if request.method == 'POST':
        # If the request is a POST, delete the task
        item.delete()
        return redirect('index')  # Redirect to the task list or another appropriate page

    # If the request is not a POST, render the confirmation page
    context = {'item': item}
    return render(request, 'delete.html', context)