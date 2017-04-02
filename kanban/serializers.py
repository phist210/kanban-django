
from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Task


class TaskSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Task
        fields = ('name', 'priority', 'status')

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
    class Meta:
        model = User
        fields = ('password', 'first_name', 'last_name', 'email')
        write_only_fields = ('password',)

    def create(self, validated_data):
            user = User(email=validated_data['email'],
                        username=validated_data['username'])
            user.set_password(validated_data['password'])
            user.save()
            return user
