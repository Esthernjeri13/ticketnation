"""
URL configuration for ticketnation project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from application import views

urlpatterns = [
      path('admin/', admin.site.urls),
      path('home/', views.home, name='home'),
    path('formulaone/', views.formulaone, name='formulaone'),
    path('mytickets/', views.mytickets, name='mytickets'),
    path('football/', views.football, name='football'),
    path('artgalas/', views.artgalas, name='artgalas'),
    path('property_single/', views.property_single, name='property_single'),
    path('service_details/', views.service_details, name='service_details'),
    path('concerts/', views.concerts, name='concerts'),
    path('starter_page/', views.starter_page, name='starter_page'),
    path('base/', views.base, name='base'),
    path('login/', views.login, name='login'),
    path('signup/', views.signup, name='signup'),
    path('ticket/', views.ticket, name='ticket'),
    path('ticketapi/', views.ticketapi, name='ticketapi'),
    path('mpesaapi/',views.mpesaapi, name='mpesaapi'),
    path('logout/', views.logout_view, name='logout'),
]
