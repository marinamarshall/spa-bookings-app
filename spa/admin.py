from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Treatment, Client, Booking


@admin.register(Treatment)
class TreatmentAdmin(SummernoteModelAdmin):
    """ TreatmentAdmin """
    list_display = ('title', 'slug', 'category')
    list_filter = ('title',)
    search_fields = ['title']
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = 'description'


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    """ ClientAdmin """
    list_display = ('first_name', 'last_name', 'client_phone')
    list_filter = ('first_name', 'last_name', 'client_phone')
    search_fields = ['first_name', 'last_name', 'client_phone']


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    """ BookingAdmin """
    list_display = ('booking_client', 'booking_treatment', 'booking_day', 'booking_time')
    list_filter = ('booking_client', 'booking_treatment', 'booking_day', 'booking_time')
    search_fields = ['booking_client', 'booking_treatment', 'booking_day', 'booking_time']
    actions = ['approve_booking']

    def approve_booking(self, request, queryset):
        """ approve booking """
        queryset.update(approved=True)
