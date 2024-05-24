from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from lpclApp.views import *

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', include('lpclApp.urls')),
    path('about', include('lpclApp.urls')),
    path('service', include('lpclApp.urls')),
    path('contact', include('lpclApp.urls')),
    path('subsidiaries', include('lpclApp.urls')),
    path('TRAVELS_SUPPORT_SERVICES', include('lpclApp.urls')),
    path('PROJECT_TECHNICAL_SERVICES', include('lpclApp.urls')),
    path('MEDIA_INNOVATION_DESIGNERS', include('lpclApp.urls')),
    path('BUSINESS_REGISTRATION_CONSULTING_SETUP', include('lpclApp.urls')),
    path('MANUFACTURING_RELATED_SERVICES_INVESTMENT_REAL_ESTATE', include('lpclApp.urls')),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
