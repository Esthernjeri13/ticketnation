from django.db import models
from django.utils.timezone import now
import uuid

# Create your models here.
class Ticket(models.Model):
    TICKET_TYPE_CHOICES = [
        ('REGULAR', 'Regular'),
        ('VIP', 'VIP'),
    ]

    PAYMENT_METHOD_CHOICES = [
        ('CREDIT_CARD', 'Credit Card'),
        ('M-PESA', 'M-Pesa'),
    ]

    name = models.CharField(max_length=255)
    ticket_type = models.CharField(max_length=10, choices=TICKET_TYPE_CHOICES)
    ticket_price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    number_of_tickets = models.PositiveIntegerField()
    payment_method = models.CharField(max_length=20, choices=PAYMENT_METHOD_CHOICES)
    date_of_purchase = models.DateTimeField(default=now)

    def __str__(self):
        return self.name

