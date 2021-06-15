from django.db import models
from django.db.models import fields
from django.contrib.auth.models import User
from rest_framework import serializers 

from .models import Task

class TaskSerializer(serializers.ModelSerializer):
    
    class Meta:
        model   = Task
        fields  = '__all__'
        # read_only_fields = ('')

    
class UserSerializer(serializers.ModelField):

    class Meta:
        model   = User


