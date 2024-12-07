from rest_framework import serializers
from application.models import Ticket

class TicketSerializer(serializers.ModelSerializer):
      class Meta:
             model= Ticket
             fields =['name', 'ticket_type', 'ticket_price', 'number_of_tickets', 'payment_method']
