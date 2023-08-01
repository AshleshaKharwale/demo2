from rest_framework.permissions import DjangoObjectPermissions
from rest_framework.viewsets import (
    ViewSet, ModelViewSet, GenericViewSet, ReadOnlyModelViewSet, ViewSetMixin
)
from rest_framework.mixins import (
    ListModelMixin, RetrieveModelMixin, CreateModelMixin, DestroyModelMixin, UpdateModelMixin
)
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.authentication import TokenAuthentication

from .models import Blog, Author
from .serializers import BlogSerializer, AuthorSerializer
from .pagination import BlogLimitOffsetPagination, AuthorCursorPagination, MyNumberPagination


# ViewSet
class BolgViewSet(ViewSet):
    queryset = Blog.objects.all()

    def list(self, request):
        self.queryset = Blog.objects.all()
        serializer = BlogSerializer(self.queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        instance = get_object_or_404(self.queryset, pk=pk)
        serializer = BlogSerializer(instance)
        return Response(serializer.data)

    def create(self, request):
        serializer = BlogSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def update(self, request, pk=None):
        instance = get_object_or_404(self.queryset, pk=pk)
        serializer = BlogSerializer(instance, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def partial_update(self, request, pk=None):
        instance = get_object_or_404(self.queryset, pk=pk)
        serializer = BlogSerializer(instance, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def destroy(self, request, pk=None):
        instance = get_object_or_404(self.queryset, pk=pk)
        instance.delete()
        return Response({'message': 'Item deleted successfully!'})


'''
# GenericViewSet - using mixins
class AuthorViewSet(ListModelMixin, RetrieveModelMixin, CreateModelMixin, UpdateModelMixin,
                    DestroyModelMixin, GenericViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
'''


# GenericViewSet - without mixins
class AuthorViewSet(GenericViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = [DjangoObjectPermissions]

    def list(self, request):
        serializer = self.get_serializer(self.get_queryset(), many=True)
        return self.get_paginated_response(self.paginate_queryset(serializer.data))

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def retrieve(self, request, pk):
        obj = self.get_object()
        serializer = self.get_serializer(obj)
        return Response(serializer.data)

    def destroy(self, request, pk):
        obj = self.get_object()
        obj.delete()
        return Response({"message": "Item deleted!"})


# ModelViewSet
class BlogModelViewSet(ModelViewSet):
    serializer_class = BlogSerializer
    queryset = Blog.objects.all()
    pagination_class = BlogLimitOffsetPagination
    permission_classes = [IsAuthenticated]
    # JWT Authentication
    authentication_classes = [JWTAuthentication]


class AuthorReadOnlyModelViewSet(ReadOnlyModelViewSet):
    serializer_class = AuthorSerializer
    queryset = Author.objects.all()
    pagination_class = AuthorCursorPagination
    permission_classes = [IsAuthenticated]
    # drf authtoken
    authentication_classes = [TokenAuthentication]
