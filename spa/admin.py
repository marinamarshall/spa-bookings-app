from django.contrib import admin
from .models import Treatment, Client, Booking
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Treatment)
class TreatmentAdmin(SummernoteModelAdmin):
    """ TreatmentAdmin """
    list_display = ('category', 'title', 'slug', 'time')
    list_filter = ('category', 'title')
    search_fields = ['category', 'title']
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = 'description'


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    """ ClientAdmin """
    list_display = ('client_name', 'client_email', 'client_phone')
    list_filter = ('client_name', 'client_email', 'client_phone')
    search_fields = ['client_name', 'client_email', 'client_phone']


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    """ BookingAdmin """
    list_display = ('booking_specification', 'booked_status')
    list_filter = ('booking_specification', 'booked_status')
    search_fields = ['booking_specification', 'booked_status']
    actions = ['approve_booking']

    def approve_booking(self, request, queryset):
        queryset.update(approved=True)
