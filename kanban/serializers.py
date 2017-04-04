
from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Task


class TaskSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Task
        fields = ('name', 'priority', 'status', 'owner_id', 'id')

    def in_range(priority):
        if priority not in range(1, 11):
            raise serializers.ValidationError('This field must '
                                              'be an integer 1-10.')

    def vaild_status(status):
        valid_list = ['backlog', 'active', 'complete']
        if status.lower() not in valid_list:
            raise serializers.ValidationError('This field must be backlog, '
                                              'active or complete.')

    priority = serializers.IntegerField(validators=[in_range])
    status = serializers.CharField(validators=[vaild_status])


class UserSerializer(serializers.ModelSerializer):

    task = serializers.PrimaryKeyRelatedField(many=True, queryset=Task.objects.all())

    class Meta:
        model = User
        fields = ('id', 'username', 'task')
