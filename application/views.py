from urllib import request

from django.contrib.auth import authenticate, logout
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, redirect
from django_daraja.mpesa.core import MpesaClient
from rest_framework import status
from rest_framework.decorators import api_view

from application.forms import TicketForm
from application.models import Ticket
from application.serializers import TicketSerializer


# Create your views here.


def home(request):
    return render(request, 'home.html')
def formulaone(request):
    return render(request, 'formulaone.html')
def football(request):
    return render(request, 'football.html')
def mytickets(request):
    data = Ticket.objects.all()
    return render(request, 'mytickets.html', {'data':data})
def artgalas(request):
    return render(request, 'artgalas.html')

def property_single(request):
    return render(request, 'property-single.html')

def concerts(request):
    return render(request, 'concerts.html')
def service_details(request):
    return render(request, 'service-details.html')
def starter_page(request):
    return render(request, 'starter-page.html')
def base(request):
    return render(request, 'base.html')
def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')  # Redirects to the home page after successful login
        else:
            return render(request, 'login.html', {'error': 'Invalid credentials'})
    return render(request, 'login.html')
def signup(request):
    return render(request, 'signup.html')
def ticket(request):
    if request.method == 'POST':
        form = TicketForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('ticket')
    else:
        form = TicketForm()
    return render(request, 'ticket.html',{'form': form})

@api_view(['GET', 'POST'])
def ticketapi(request):
    if request.method =='GET':
        tickets = Ticket.objects.all()
        serializer = TicketSerializer(tickets, many=True)
        return JsonResponse(serializer.data, safe=False)
    elif request.method =='POST':
        serializer = TicketSerializer(data=request.data)
        if serializer.is_valid():
               serializer.save()
               return JsonResponse(serializer.data,status=status.HTTP_201_CREATED)
        return JsonResponse(serializer.error,status=status.HTTP_400_BAD_REQUEST)

def mpesaapi(request):
    client = MpesaClient()
    phone_number = '0728141722'
    amount = 1000
    account_reference = 'Ticket Purchase'
    transaction_desc = 'The Eras Tour 2024'
    callback_url = 'https://darajambili.herokuapp.com/express-payment'
    response = client.stk_push(phone_number,amount,account_reference,transaction_desc,callback_url)
    return HttpResponse(response)
def logout_view(request):
    logout(request)
    return redirect('login')