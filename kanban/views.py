from django.http import Http404
from django.shortcuts import redirect, render
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from rest_framework import viewsets
from .models import Task
from .serializers import TaskSerializer, UserSerializer
from rest_framework import generics
from .forms import TaskForm
from django.contrib.auth.models import User


def index(request):
    try:
        task = Task.objects.filter(owner_id=request.user.id)
    except Task.DoesNotExist:
        raise Http404("Task does not exist")
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.owner = request.user
            task.save()
            return redirect('/kanban/', pk=task.pk)
    else:
        form = TaskForm()
    return render(request, 'kanban/index.html', {'task': task, "form": form})


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('/kanban')
    else:
        form = UserCreationForm()
    return render(request, 'kanban/signup.html', {'form': form})


def edit_task(request, id):
    try:
        task = Task.objects.get(id=id)
    except Task.DoesNotExist:
        raise Http404("Task does not exist")

    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            task = form.save(commit=True)
            task.save()
            return redirect('/kanban/', pk=task.pk)

    else:
        form = TaskForm(instance=task)
    return render(request, 'kanban/edit_task.html', {'form': form, 'task': task})


def delete_task(request, id):
    task = Task.objects.get(id=id)
    task.delete()
    url = 'kanban/delete_task.html'
    return render(request, url, {'task': task})


class TaskViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows abilities to be viewed or edited.
    """
    serializer_class = TaskSerializer

    def get_queryset(self):
        return Task.objects.filter(owner_id=self.request.user.id).order_by('-status')


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
