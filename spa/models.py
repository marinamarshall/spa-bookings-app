from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

BOOKED = ((0, "Unconfirmed"), (1, "Booked"))


class Treatment(models.Model):
    """ treatments """
    featured_image = CloudinaryField('image', default='placeholder')
    title = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=50, unique=True)
    category = models.CharField(max_length=15)
    description = models.TextField()
    # booking_duration = models.TimeField()
    status = BOOKED
    # time = models.DateTimeField()

    # class Meta:

    def __str__(self):
        return f"Treatment: {self.title} Added"


class Client(models.Model):
    """ client """
    # client_id = models.IntegerField()
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    client_phone = models.IntegerField()
    is_staff = False
    treatment_receiving = models.ForeignKey(
        Treatment, on_delete=models.CASCADE, related_name="client_treatments")

    def __str__(self):
        return f"New client added: {self.first_name} {self.last_name}, {self.client_phone}, {self.email}"


class Booking(models.Model):
    """ booking """
    # booking_id = models.ForeignKey(
    #     Client, on_delete=models.CASCADE, related_name="client_treatments")
    booking_client = models.ForeignKey(Client, on_delete=models.CASCADE)
    booking_treatment = models.ForeignKey(Treatment, on_delete=models.CASCADE)
    booking_day = models.DateField()
    booking_time = models.TimeField()
    booked_status = models.IntegerField(choices=BOOKED, default=0)

    def __str__(self):
        return f"{self.booking_client} has booked {self.booking_treatment} for {self.booking_day} at {self.booking_time}"
