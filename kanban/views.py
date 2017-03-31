from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import Http404
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from rest_framework import viewsets
from .models import Task

from .serializers import TaskSerializer
from django.views.decorators.csrf import csrf_protect


def index(request):
    try:
        task = Task.objects.all()
    except Task.DoesNotExist:
        raise Http404("Task does not exist")
    return render(request, 'kanban/index.html', {'task': task})


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('/task')
    else:
        form = UserCreationForm()
    return render(request, 'kanban/signup.html', {'form': form})


class TaskViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows abilities to be viewed or edited.
    """
    queryset = Task.objects.all().order_by('-priority')
    serializer_class = TaskSerializer


@csrf_protect
@api_view(['GET', 'POST'])
def task_list(request, pk):
    """
    List all snippets, or create a new snippet.
    """

    if request.method == 'GET':
        task = Task.objects.all()
        serializer = TaskSerializer(task, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def task_detail(request, pk):
    """
    Retrieve, update or delete a snippet instance.
    """
    try:
        task = Task.objects.get(pk=pk)
    except Task.DoesNotExist:

        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = TaskSerializer(task)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = TaskSerializer(task, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        task.destroy()
        return Response(status=status.HTTP_204_NO_CONTENT)
