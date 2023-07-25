from django.http import Http404
from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import permissions

from .models import Todo
from .serializers import TodoSerializer


# Create your views here.


class TodoAPIView(APIView):
    # basic authentication
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, id=None):
        if id is not None:
            # detail view
            try:
                data = Todo.objects.get(pk=id)
                serializer = TodoSerializer(data)
                return Response(serializer.data, status=status.HTTP_200_OK)
            except:
                raise Http404("Id does not exist!")

        # list view
        data = Todo.objects.all()
        serializer = TodoSerializer(data, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = TodoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, id):
        try:
            todo_id = Todo.objects.get(pk=id)
            serializer = TodoSerializer(todo_id, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except:
            raise Http404()

    def patch(self, request, id):
        try:
            todo_id = Todo.objects.get(pk=id)
            serializer = TodoSerializer(todo_id, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except:
            raise Http404("Id does not exist")

    def delete(self, request, id):
        try:
            item = Todo.objects.get(pk=id)
            item.delete()
            return Response({'message': f'{id} got deleted!'})
        except:
            return Response({'message': 'requested id does not exist!'})
