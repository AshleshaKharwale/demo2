from django.http import Http404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.core.exceptions import ObjectDoesNotExist

from .models import Todo
from .serializers import TodoSerializer


@api_view(['GET', 'POST', 'PUT', 'PATCH', 'DELETE'])
def todo_api_view(request, pk=None):

    if request.method == 'GET':
        if pk is not None:
            try:
                data = Todo.objects.get(pk=pk)
                serializer = TodoSerializer(data)
                return Response(serializer.data, status=status.HTTP_200_OK)
            except ObjectDoesNotExist as e:
                return Response({'error': 'Id does not exist'}, status=status.HTTP_404_NOT_FOUND)

        data = Todo.objects.all()
        serializer = TodoSerializer(data, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    elif request.method == 'POST':
        data = request.data
        serializer = TodoSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'PUT':
        try:
            todo_obj = Todo.objects.get(pk=pk)
            serializer = TodoSerializer(todo_obj, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except ObjectDoesNotExist as e:
            return Response({'error': 'Id does not exist'}, status=status.HTTP_404_NOT_FOUND)

    elif request.method == 'PATCH':
        try:
            todo_obj = Todo.objects.get(pk=pk)
            serializer = TodoSerializer(todo_obj, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except ObjectDoesNotExist as e:
            raise Http404
            # return Response({'error': e}, status=status.HTTP_404_NOT_FOUND)
