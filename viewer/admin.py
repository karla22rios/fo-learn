from django.contrib import admin
from .models import Category, Lesson, Step, Asset3D

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    search_fields = ("name",)

class StepInline(admin.TabularInline):
    model = Step
    extra = 1

@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ("title", "category", "order")
    list_filter = ("category",)
    search_fields = ("title", "summary")
    prepopulated_fields = {"slug": ("title",)}
    inlines = [StepInline]

@admin.register(Asset3D)
class Asset3DAdmin(admin.ModelAdmin):
    list_display = ("title", "created_at")
    search_fields = ("title",)

@admin.register(Step)
class StepAdmin(admin.ModelAdmin):
    list_display = ("lesson", "order", "title", "has_audio")
    list_filter = ("lesson",)
    search_fields = ("title", "description", "tts_text")
    fields = ("lesson", "order", "title", "description", "asset", "audio", "tts_text")

    def has_audio(self, obj):
        return bool(obj.audio)
    has_audio.boolean = True
    has_audio.short_description = "Audio"
