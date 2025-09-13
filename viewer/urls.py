from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("c/<slug:slug>/", views.category_detail, name="category_detail"),
    path("l/<slug:slug>/", views.lesson_detail, name="lesson_detail"),
    path("step/<int:pk>/", views.step_viewer, name="step_viewer"),
]
