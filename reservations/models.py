from django.db import models
from customers.models import Customer
from tables.models import Table


class Reservation(models.Model):
    STATUS_CHOICES = [
        ("pending", "Pending"),
        ("confirmed", "Confirmed"),
        ("canceled", "Canceled"),
    ]

    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)   
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=20)  
    table = models.ForeignKey(Table, on_delete=models.CASCADE)  
    date = models.DateTimeField()  
    comment = models.TextField(blank=True, null=True)  
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default="pending")  

    def __str__(self):
        return f"Reservation by {self.customer} on {self.date}"
