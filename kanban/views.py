from django.http import Http404
from django.shortcuts import redirect, render
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from rest_framework import viewsets
from .models import Task
from .serializers import TaskSerializer, UserSerializer
from rest_framework import generics
from .forms import TaskForm, EditTaskForm
from django.contrib.auth.models import User


<<<<<<< HEAD
# def new_task(request):
#     if request.method == 'POST':
#         form = TaskForm(request.POST)
#         if form.is_valid():
#             task = form.save(commit=False)
#             task.owner = request.user
#             task.save()
#             return redirect('/kanban/', pk=task.pk)
#     else:
#         form = TaskForm()
#     return render(request, 'kanban/new_task.html', {'form': form})
=======
def edit_task(request):
    pass
>>>>>>> 884adccd0e5a5dd9858adb8e6436c5d8992d36ed


def index(request):
    try:
<<<<<<< HEAD
        task = Task.objects.filter(owner_id=request.user.id)
=======
        task = Task.objects.filter(owner=1).order_by('-priority')
>>>>>>> 884adccd0e5a5dd9858adb8e6436c5d8992d36ed
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
<<<<<<< HEAD
    return render(request, 'kanban/index.html', {'task': task, "form": form})
=======

    return render(request, 'kanban/index.html', {'task': task, 'form': form})
>>>>>>> 884adccd0e5a5dd9858adb8e6436c5d8992d36ed


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
<<<<<<< HEAD
=======


# @csrf_protect
# @api_view(['GET', 'POST'])
# def task_list(request, pk):
#     """
#     List all snippets, or create a new snippet.
#     """
#
#     if request.method == 'GET':
#         task = Task.objects.all()
#         serializer = TaskSerializer(task, many=True)
#         return Response(serializer.data)
#
#     elif request.method == 'POST':
#         serializer = TaskSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#
# @api_view(['GET', 'PUT', 'DELETE'])
# def task_detail(request, pk):
#     """
#     Retrieve, update or delete a snippet instance.
#     """
#
#     task = Task.get_object_or_404(pk=pk)
#
#     if request.method == 'GET':
#         serializer = TaskSerializer(task)
#         return Response(serializer.data)
#
#     elif request.method == 'PUT':
#         serializer = TaskSerializer(task, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     elif request.method == 'DELETE':
#         task.destroy()
#         return Response(status=status.HTTP_204_NO_CONTENT)
>>>>>>> 884adccd0e5a5dd9858adb8e6436c5d8992d36ed
