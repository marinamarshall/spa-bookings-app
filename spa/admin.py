from django.contrib import admin
from .models import Treatment, Client, Booking
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Treatment)
class TreatmentAdmin(SummernoteModelAdmin):
    list_display = ('category', 'title', 'slug', 'time')
    search_fields = ['category', 'title']
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = 'description'

