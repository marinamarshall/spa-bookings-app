from django.shortcuts import render
from django.views import generic
from .models import Treatment

class TreatmentList(generic.ListView):
    """ TreatmentList """
    model = Treatment
    queryset = Treatment.objects.filter(status=1)
    template_name = 'index.html'
    paginate_by = 9
