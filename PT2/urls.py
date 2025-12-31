from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.views.static import serve
from rest_framework.routers import DefaultRouter
from viewer.api import CategoryView, LessonView, StepView, AssetView

router = DefaultRouter()
router.register(r"api/categories", CategoryView, basename="api-categories")
router.register(r"api/lessons", LessonView, basename="api-lessons")
router.register(r"api/steps", StepView, basename="api-steps")
router.register(r"api/assets", AssetView, basename="api-assets")

urlpatterns = [
   re_path(r"^media/(?P<path>.*)$", serve, {"document_root": settings.MEDIA_ROOT}),
    path("admin/", admin.site.urls),
    path("", include("viewer.urls")),
    path("", include(router.urls)),
]

#urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)