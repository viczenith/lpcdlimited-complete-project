from django.urls import path
from .views import *

urlpatterns = [
    path('', HOME, name='home_page'),
    path('about', ABOUT, name='about_page'),
    path('service', SERVICE, name='service_page'),
    path('contact', CONTACT, name='contact_page'),
    path('subsidiaries', SUBSIDIARIES, name='subsidiaries_page'),
    path('TRAVELS_SUPPORT_SERVICES', TRAVELS_SUPPORT_SERVICES, name='TRAVELS_SUPPORT_SERVICES_page'),
    path('PROJECT_TECHNICAL_SERVICES', PROJECT_TECHNICAL_SERVICES, name='PROJECT_TECHNICAL_SERVICES_page'),
    path('MEDIA_INNOVATION_DESIGNERS', MEDIA_INNOVATION_DESIGNERS, name='MEDIA_INNOVATION_DESIGNERS_page'),
    path('BUSINESS_REGISTRATION_CONSULTING_SETUP', BUSINESS_REGISTRATION_CONSULTING_SETUP, name='BUSINESS_REGISTRATION_CONSULTING_SETUP_page'),
    path('MANUFACTURING_RELATED_SERVICES_INVESTMENT_REAL_ESTATE', MANUFACTURING_RELATED_SERVICES_INVESTMENT_REAL_ESTATE, name='MANUFACTURING_RELATED_SERVICES_INVESTMENT_REAL_ESTATE_page'),
    
]