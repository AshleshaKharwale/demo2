from rest_framework import serializers

from .models import Todo


'''
class TodoSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=100)
    description = serializers.CharField(max_length=500, allow_blank=True)
    completed = serializers.BooleanField(default=False)

    def create(self, validated_data):
        return Todo.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.description = validated_data.get('description', instance.description)
        instance.completed = validated_data.get('completed', instance.completed)
        instance.save()
        return instance
'''

class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = '__all__'