from django import forms
from .models import Asset3D

class Asset3DForm(forms.ModelForm):
    class Meta: model = Asset3D; fields = ["title","description","file"]
    def clean_file(self):
        f = self.cleaned_data["file"]
        if not f.name.lower().endswith((".glb",".gltf")):
            raise forms.ValidationError("Formato permitido: .glb o .gltf")
        if f.size > 25 * 1024 * 1024:
            raise forms.ValidationError("El archivo excede 25MB (optimiza el modelo).")
        return f
