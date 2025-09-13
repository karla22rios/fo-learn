from rest_framework import viewsets, mixins
from .models import Category, Lesson, Step, Asset3D
from .serializers import CategorySerializer, LessonSerializer, StepSerializer, Asset3DSerializer

class CategoryView(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    lookup_field = "slug"

class LessonView(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    queryset = Lesson.objects.prefetch_related("steps__asset").select_related("category")
    serializer_class = LessonSerializer
    lookup_field = "slug"

class StepView(mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    queryset = Step.objects.select_related("asset", "lesson", "lesson__category")
    serializer_class = StepSerializer

class AssetView(mixins.RetrieveModelMixin, mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = Asset3D.objects.all()
    serializer_class = Asset3DSerializer
