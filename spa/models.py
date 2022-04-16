from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

BOOKED = ((0, "Unconfirmed"), (1, "Booked"))


class Treatment(models.Model):
    """ treatments """
    featured_image = CloudinaryField('image', default='placeholder')
    category = models.CharField(max_length=15)
    title = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=50, unique=True)
    description = models.TextField()
    time = models.DateTimeField(unique=True)

    # class Meta:

    def __str__(self):
        return f"Treatment: {self.title}, booked for: {self.time}"


class Client(models.Model):
    """ client """
    # treatment = models.ForeignKey(
    #     Treatment, on_delete=models.CASCADE, related_name="client_treatments")
    # client_id = models.IntegerField()
    client_name = models.CharField(max_length=50)
    client_email = models.EmailField(unique=True)
    client_phone = models.IntegerField()

    def __str__(self):
        return f"New client added: {self.client_name} {self.client_phone} {self.client_email}"


class Booking(models.Model):
    """ booking """
    # booking_id = models.ForeignKey(
    #     Client, on_delete=models.CASCADE, related_name="client_treatments")
    booking_specification = models.DateTimeField(unique=True)
    # booking_time = models.DurationField()
    booked_status = models.IntegerField(choices=BOOKED, default=0)

    def __str__(self):
        return f"Your booking for {self.booking_specification} has been {self.booked_status}"
