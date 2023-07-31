from rest_framework.serializers import ModelSerializer, HyperlinkedModelSerializer

from .models import Blog, Author


class BlogSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Blog
        fields = '__all__'


class AuthorSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'
