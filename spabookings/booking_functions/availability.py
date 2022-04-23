import datetime
from spa.models import Treatment, Client, Booking


def check_availability(booking_treatment, booking_day, booking_time):
    """ check_availability """
    available_apps = []
    booking_list = Treatment.objects.filter(booking_treatment=booking_treatment)

    for booking in booking_list:
        if booking.booking_time > booking.booking_duration or booking.booking_time < booking.booking_duration:
            available_apps.append(True)
        else:
            available_apps.append(False)
