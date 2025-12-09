from django.shortcuts import render, get_object_or_404
from .models import Category, Lesson, Step

def home(request):
    categories = Category.objects.all().order_by("name")
    return render(request, "viewer/home.html", {"categories": categories})

def category_detail(request, slug):
    category = get_object_or_404(Category, slug=slug)
    lessons = category.lessons.all()
    return render(request, "viewer/category_detail.html", {"category": category, "lessons": lessons})

def lesson_detail(request, slug):
    lesson = get_object_or_404(Lesson, slug=slug)
    steps = lesson.steps.select_related("asset").all()
    return render(request, "viewer/lesson_detail.html", {"lesson": lesson, "steps": steps})

def step_viewer(request, pk):
    step = get_object_or_404(Step, pk=pk)
    steps = Step.objects.filter(lesson=step.lesson).order_by("order")
    idx = list(steps).index(step)
    prev_step = steps[idx-1] if idx > 0 else None
    next_step = steps[idx+1] if idx < len(steps)-1 else None
    return render(request, "viewer/step_viewer.html", {
        "step": step, "steps": steps,
        "prev_step": prev_step, "next_step": next_step
    })

