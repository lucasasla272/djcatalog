from django import forms
from .models import DJ


class DJForm(forms.ModelForm):
    class Meta:
        model = DJ
        fields = ['nombre', 'estilo', 'nacionalidad', 'debut_year', 'descripcion']

    # Validación personalizada: el año de debut no puede ser futuro
    def clean_debut_year(self):
        anio = self.cleaned_data['debut_year']
        from datetime import date
        if anio > date.today().year:
            raise forms.ValidationError("El año de debut no puede ser futuro.")
        return anio