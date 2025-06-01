from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Destination(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    location= models.CharField(max_length=1000)
    image = models.ImageField(upload_to='destinations/', null=True, blank=True)


    def __str__(self):
        return self.name
    

class Trip(models.Model):
    destination = models.ForeignKey(Destination, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    available_seats = models.IntegerField()

    def __str__(self):
        return f"{self.destination.name} ({self.start_date} to {self.end_date})"
    
class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    trip = models.ForeignKey(Trip, on_delete=models.CASCADE)
    booking_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length = 100, choices=[
        ('pending', 'Pending'),
        ('confirmed', 'Confirmed'),
        ('cancelled', 'Cancelled')
    ], default='pending')

    def str(self):
        return f"{self.user.username} - {self.trip}"
    
