from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Task


class TaskSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Task
        fields = ('name', 'description', 'status', 'owner_id', 'id')

    def vaild_status(status):
        valid_list = ['backlog', 'active', 'complete']
        if status.lower() not in valid_list:
            raise serializers.ValidationError('This field must be backlog, '
                                              'active or complete.')

    description = serializers.CharField()
    status = serializers.CharField(validators=[vaild_status])


class UserSerializer(serializers.ModelSerializer):

    task = serializers.PrimaryKeyRelatedField(many=True,
                                              queryset=Task.objects.all())

    class Meta:
        model = User
        fields = ('id', 'username', 'task')
