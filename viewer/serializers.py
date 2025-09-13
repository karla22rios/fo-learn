from rest_framework import serializers
from .models import Category, Lesson, Step, Asset3D

class Asset3DSerializer(serializers.ModelSerializer):
    class Meta:
        model = Asset3D
        fields = ["id", "title", "description", "file", "created_at"]

class StepSerializer(serializers.ModelSerializer):
    asset = Asset3DSerializer()
    class Meta:
        model = Step
        fields = ["id", "order", "title", "description", "asset"]

class LessonSerializer(serializers.ModelSerializer):
    steps = StepSerializer(many=True)
    category = serializers.StringRelatedField()
    class Meta:
        model = Lesson
        fields = ["id","title","slug","summary","order","category","steps"]

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["id","name","slug"]
