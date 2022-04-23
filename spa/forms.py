from .models import Treatment
from django import forms


class TreatmentForm(forms.ModelForm):
    """ TreatmentForm """
    class Meta:
        """ Meta """
        model = Treatment
        fields = ('description',)