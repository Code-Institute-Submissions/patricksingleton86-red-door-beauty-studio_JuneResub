from django.db import models

# Create your models here.
# class Customer(models.Model):
#     full_name = models.CharField(max_length=50, null=False, blank=False)
#     email = models.EmailField(max_length=254, null=False, blank=False)
#     phone_number = models.CharField(max_length=20, null=False, blank=False)

# class ServiceType(models.Model):
#     treatment = models.ForeignKey('Treatment', null=True, blank=True, on_delete=models.SET_NULL)

# class Reservation(models.Model):
#     treatment = models.ForeignKey('Treatment', null=True, blank=True, on_delete=models.SET_NULL)
#     full_name = models.CharField(max_length=50, null=False, blank=False)
#     booked_for = models.DateField()