from rest_framework.generics import (
    ListAPIView, ListCreateAPIView, DestroyAPIView, RetrieveUpdateDestroyAPIView,
    RetrieveDestroyAPIView, RetrieveUpdateAPIView, UpdateAPIView, GenericAPIView,
    RetrieveAPIView, CreateAPIView
)
from rest_framework.permissions import IsAuthenticated
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework.settings import api_settings
from rest_framework.mixins import (
    ListModelMixin, CreateModelMixin, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin
)

from .models import Todo
from .serializers import TodoSerializer


QUERYSET = Todo.objects.all()
# Pagination default settings gets applied to ListView and ListCreateAPIView.


class ListView(ListAPIView):
    # queryset = QUERYSET.filter(completed=False)  # to list only non-completed todoo items
    queryset = QUERYSET.filter(completed=False)
    serializer_class = TodoSerializer
    permission_classes = [IsAuthenticated]


class DetailView(RetrieveAPIView):
    queryset = QUERYSET
    serializer_class = TodoSerializer
    permission_classes = [IsAuthenticated]


class UpdateView(UpdateAPIView):
    # put and patch both requests
    queryset = QUERYSET
    serializer_class = TodoSerializer
    permission_classes = [IsAuthenticated]


class CreateView(CreateAPIView):
    serializer_class = TodoSerializer
    permission_classes = [IsAuthenticated]


class DeleteView(DestroyAPIView):
    queryset = QUERYSET
    permission_classes = [IsAuthenticated]


class ListCreateView(ListCreateAPIView):
    queryset = QUERYSET
    serializer_class = TodoSerializer
    permission_classes = [IsAuthenticated]


class DetailUpdateView(RetrieveUpdateAPIView):
    queryset = QUERYSET
    serializer_class = TodoSerializer
    permission_classes = [IsAuthenticated]
    # renderer_classes = [JSONRenderer]  # to return data in JSON format


class DetailDeleteView(RetrieveDestroyAPIView):
    queryset = QUERYSET
    permission_classes = [IsAuthenticated]


class DetailUpdateDeleteView(RetrieveUpdateDestroyAPIView):
    queryset = QUERYSET
    serializer_class = TodoSerializer
    permission_classes = [IsAuthenticated]


class GenericListCreateView(ListModelMixin, CreateModelMixin, GenericAPIView):
    queryset = QUERYSET
    serializer_class = TodoSerializer
    permission_classes = [IsAuthenticated]
    pagination_class = api_settings.DEFAULT_PAGINATION_CLASS

    '''
    # without mixins
    def get(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
    '''

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class GenericDetailUpdateDeleteView(RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin,
                                    GenericAPIView):
    queryset = QUERYSET
    serializer_class = TodoSerializer
    permission_classes = [IsAuthenticated]
    pagination_class = api_settings.DEFAULT_PAGINATION_CLASS

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
