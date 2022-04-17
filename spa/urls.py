from django.urls import path
from . import views

urlpatterns = [
    path('', views.TreatmentList.as_view(), name='home'),
    ]
