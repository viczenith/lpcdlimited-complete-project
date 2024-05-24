from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages
from .models import *
from django.http import HttpResponseRedirect

def HOME(request):
    template = 'index.html'
    imageSlider = Home_Page_Slider.objects.all()
    aboutusvideo = About_Us_Video.objects.first()
    mission_and_vison = Mission_and_Vison.objects.all()
    context = {
        'imageSlider': imageSlider,
        'aboutusvideo': aboutusvideo,
        'mission_and_vison': mission_and_vison,
    }
    return render(request, template, context)


def ABOUT(request):
    template = 'about.html'
    aboutusvideo = About_Us_Video.objects.first()
    mission_and_vison = Mission_and_Vison.objects.all()
    context = {
        'aboutusvideo': aboutusvideo,
        'mission_and_vison': mission_and_vison,
    }
    return render(request, template, context)


def SERVICE(request):
    template = 'service.html'
    return render(request, template)


def CONTACT(request):
    template = 'contact.html'
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone_number = request.POST.get('phone_number')
        message = request.POST.get('message')

        if not message:
            messages.error(request, 'Message cannot be empty. Please enter a message.')
        else:
            # Save the data to the database
            user_request = ContactMessage(
                name=name,
                email=email,
                phone_number=phone_number,
                message=message
            )
            user_request.save()

            if user_request.id:
                messages.success(request, f'Hello {name}, Your message has been sent successfully! We\'ll get back to you shortly')
                return HttpResponseRedirect(request.path_info)
            else:
                messages.error(request, 'There was an error in your form. Please correct it and try again.')
                
    else:
        return render(request, template)


# def CONTACT(request):
#     template = 'contact.html'
#     if request.method == 'POST':
#         name = request.POST.get('name')
#         email = request.POST.get('email')
#         phone_number = request.POST.get('phone_number')
#         message = request.POST.get('message')

#         if not message:  # Check if message is empty
#             messages.error(request, 'Message cannot be empty. Please enter a message.')
#         else:
#             # Save the data to the database
#             user_request = ContactMessage(
#                 name=name,
#                 email=email,
#                 phone_number=phone_number,
#                 message=message
#             )
#             user_request.save()

#             if user_request.id:
#                 # Send email notification to user
#                 subject = 'Message Received'
#                 message_body = f'Hello {name},\n\nThank you for contacting us. We have received your message and will get back to you shortly.\n\nBest regards,\nThe Team'
#                 sender_email = settings.EMAIL_HOST_USER
#                 recipient_list = [email]

#                 send_mail(subject, message_body, sender_email, recipient_list)

#                 # Send email notification to admin
#                 admin_subject = 'New Message from Contact Form'
#                 admin_message_body = f'Name: {name}\nEmail: {email}\nPhone Number: {phone_number}\nMessage: {message}'
#                 admin_sender_email = settings.EMAIL_HOST_USER
#                 admin_recipient_list = [settings.ADMIN_EMAIL]

#                 send_mail(admin_subject, admin_message_body, admin_sender_email, admin_recipient_list)

#                 messages.success(request, f'Hello {name}, Your message has been sent successfully! We\'ll get back to you shortly')
#                 return HttpResponseRedirect(request.path_info)
#             else:
#                 messages.error(request, 'There was an error in your form. Please correct it and try again.')
#     else:
#         return render(request, template)



def SUBSIDIARIES(request):
    template = 'subsidiaries.html'
    return render(request, template)


def TRAVELS_SUPPORT_SERVICES(request):
    template = 'TravelSupportServices.html'
    travel_support_ervices = Travel_Support_Service.objects.all()
    context = {
        'travel_support_ervices':travel_support_ervices,
    }
    return render(request, template, context)

def PROJECT_TECHNICAL_SERVICES(request):
    template = 'ProjectsandTechnicalServices.html'
    projects_and_technical_services = Projects_and_Technical_Service.objects.all()
    context = {
        'projects_and_technical_services':projects_and_technical_services,
    }
    return render(request, template, context)


def MEDIA_INNOVATION_DESIGNERS(request):
    template = 'MediaandInnovativeDesigners.html'
    media_and_innovative_designers = Media_and_Innovative_Designer.objects.all()
    context = {
        'media_and_innovative_designers':media_and_innovative_designers,
    }
    return render(request, template, context)


def BUSINESS_REGISTRATION_CONSULTING_SETUP(request):
    template = 'BusinessRegistrationConsultingSetup.html'
    business_registration_consulting_setup = Business_Registration_Consulting_Setup.objects.all()
    context = {
        'business_registration_consulting_setup':business_registration_consulting_setup,
    }
    return render(request, template, context)


def MANUFACTURING_RELATED_SERVICES_INVESTMENT_REAL_ESTATE(request):
    template = 'ManufacturingandRelatedServicesInvestmentinRealEstate.html'
    manufacturing_and_related_service = Manufacturing_and_Related_Service.objects.all()
    context = {
        'manufacturing_and_related_service':manufacturing_and_related_service,
    }
    return render(request, template, context)