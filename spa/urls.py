from django.urls import path
from . import views

urlpatterns = [
    path('', views.TreatmentList.as_view(), name='home'),
    path('treatment/<int:pk/>', TreatmentDetail.as_view(), name='treatment_detail'),
    ]
