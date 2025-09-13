from django.test import TestCase
from viewer.models import Category, Lesson, Asset3D, Step

class ModelSmokeTest(TestCase):
    def test_create_minimal_graph(self):
        c = Category.objects.create(name="Fibra Óptica", slug="fibra")
        l = Lesson.objects.create(category=c, title="Cierre FOSC", slug="cierre-fosc", order=1)
        a = Asset3D.objects.create(title="Domo", description="Domo del cierre", file="models/domo.glb")
        s = Step.objects.create(lesson=l, title="Preparación", order=1, asset=a)
        self.assertEqual(l.steps.count(), 1)
        self.assertEqual(str(s), "Cierre FOSC · 1. Preparación")
