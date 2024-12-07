from django import forms

from application.models import Ticket


class TicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ['name', 'ticket_type', 'number_of_tickets', 'ticket_price', 'payment_method']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter name of event'}),
            'ticket_type': forms.Select(attrs={'class': 'form-control'}),
            'number_of_tickets': forms.NumberInput(attrs={'class': 'form-control'}),
            'ticket_price': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter ticket price'}),
            'payment_method': forms.Select(attrs={'class': 'form-control'}),
        }