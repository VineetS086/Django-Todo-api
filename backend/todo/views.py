from copy import error
from django.db.models import manager
from django.shortcuts import get_list_or_404, get_object_or_404, render

from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Task
from .serializer import TaskSerializer, UserSerializer
from .permissions import IsOwner, IsOwnerOrRead
from todo import serializer


class TaskViewList(APIView):
    permission_classes = [IsOwner]

    def get_user(self, request):
        return request.user

    def get(self, request):
        queryset    = get_list_or_404(Task, user=request.user)
        serializer  = TaskSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer  = TaskSerializer(data=request.data, context={'request':request})

        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=200)
        return Response(serializer.errors, status=400)


class TaskViewDetail(APIView):
    permission_classes = [IsOwnerOrRead]

    def get_object(self, id):
        return get_object_or_404(Task, id=id)

    def get(self, requset, id):
        task        = self.get_object(id)
        serializer  = TaskSerializer(task)
        return Response(serializer.data)

    def put(self, request, id):
        task        = self.get_object(id)
        serializer  = TaskSerializer(task, data=request.data, context={'request':request})

        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def delete(self, request, id):
        task        = self.get_object(id)
        task.delete()
        return Response(status=204)


class ReqisterView(APIView):

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            return Response(serializer.data, status=200)
        
        return Response(serializer.errors, status=400)
