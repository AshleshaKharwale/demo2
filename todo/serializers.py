from rest_framework import serializers

from .models import Todo


class TodoSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=100)
    description = serializers.CharField(max_length=500, allow_blank=True)
    completed = serializers.BooleanField(default=False)

    def create(self, validated_data):
        return Todo.objects.create(**validated_data)
