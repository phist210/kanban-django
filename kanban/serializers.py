
from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Task


class TaskSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Task
        fields = ('name', 'priority', 'status')


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('password', 'first_name', 'last_name', 'email')
        write_only_fields = ('password',)

    def create(self, validated_data):
            user = User(email=validated_data['email'], username=validated_data['username'])
            user.set_password(validated_data['password'])
            user.save()
            return user
