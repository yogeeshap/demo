from django.contrib import admin
from django.urls import path
from .views import contact_form

app_name = 'demo_app'
urlpatterns = [
    path('contact/', contact_form,name='contact'),
]
