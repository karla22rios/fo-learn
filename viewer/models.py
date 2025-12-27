from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=80, unique=True)
    slug = models.SlugField(max_length=100, unique=True)

    def __str__(self): return self.name

class Lesson(models.Model):
    category = models.ForeignKey(Category, on_delete=models.PROTECT, related_name="lessons")
    title = models.CharField(max_length=160)
    slug = models.SlugField(max_length=180, unique=True)
    summary = models.TextField(blank=True)
    order = models.PositiveIntegerField(default=1)

    class Meta:
        ordering = ["order", "id"]

    def __str__(self): return self.title

class Asset3D(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField(blank=True)

    file = models.FileField(upload_to="models/", blank=True, null=True, help_text="(Opcional) Para local. En Render usa static_path.")

    static_path = models.CharField(
        max_length=255,
        blank=True,
        help_text='Ruta en static. Ej: viewer/models/cierre.glb'
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self): 
        return self.title


class AssetFile(models.Model):
    title = models.CharField(max_length=200)
    file = models.FileField(upload_to="assets/files/")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Step(models.Model):
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, related_name="steps")
    title = models.CharField(max_length=160)
    description = models.TextField(blank=True, default="")
    order = models.PositiveIntegerField(default=1)

    asset = models.ForeignKey(
        Asset3D, on_delete=models.SET_NULL, null=True, blank=True,
        help_text="Modelo 3D asociado a este paso"
    )

    # (opcional) para local / migración
    audio = models.FileField(
        upload_to="audio/steps/",
        blank=True, null=True,
        help_text="(Opcional) Para local. En Render usa audio_static_path."
    )

    # NUEVO: ruta dentro de static/, por ejemplo: "viewer/audio/paso1.mp3"
    audio_static_path = models.CharField(
        max_length=255,
        blank=True,
        help_text='Ruta en static. Ej: viewer/audio/paso1.mp3'
    )

    tts_text = models.TextField(blank=True, help_text="(Opcional) Texto para TTS si no subes audio.")

    class Meta:
        ordering = ["order", "id"]
        unique_together = [("lesson", "order")]

    def __str__(self): 
        return f"{self.lesson.title} · {self.order}. {self.title}"

