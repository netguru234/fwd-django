from django.db import models
from django_countries.fields import CountryField
from random import randint


class Shipment(models.Model):
    tracking_number = models.CharField(
        max_length=50, verbose_name="Tracking Number", blank=True, null=True)
    receiver_name = models.CharField(
        max_length=50, verbose_name="Receiver Name")
    receiver_address = models.CharField(
        max_length=120, verbose_name="Receiver Address")
    receiver_city = models.CharField(
        max_length=50, verbose_name="Receiver City")
    receiver_state = models.CharField(
        max_length=50, verbose_name="Receiver State")
    receiver_country = CountryField()
    sender_name = models.CharField(max_length=50, verbose_name="Sender Name")
    sender_address = models.CharField(
        max_length=120, verbose_name="Sender Address")
    sender_city = models.CharField(max_length=50, verbose_name="Sender City")
    sender_state = models.CharField(max_length=50, verbose_name="Sender State")
    sender_country = CountryField()

    def __str__(self):
        return f"{self.receiver_name} - {self.tracking_number}"

    def save(self, *args, **kwargs):
        self.tracking_number = self.receiver_name[0:3] + \
            str(randint(13572, 25763820))
        return super().save(*args, **kwargs)


class History(models.Model):
    current_location = CountryField()
    arrived_at = models.DateTimeField()
    shipment = models.ForeignKey(
        Shipment, related_name='histories', on_delete=models.CASCADE)
    arrival_status = models.CharField(max_length=250)

    def __str__(self):
        return f"{self.shipment} Arrived {self.current_location} at {self.arrived_at}"

    class Meta:
        verbose_name = 'Shipment Status'
        verbose_name_plural = 'Shipment Statuses'
