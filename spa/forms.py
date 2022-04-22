from .models import Treatment
from django import forms


class TreatmentForm(forms.ModelForm):
    class Meta:
        model = Treatment
        fields = ('description',)