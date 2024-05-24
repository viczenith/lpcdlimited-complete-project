from django.db import models
from embed_video.fields import EmbedVideoField

# Create your models here.
class Home_Page_Slider(models.Model):
    slider = models.ImageField(upload_to='slider_images/')

class About_Us_Video(models.Model):
    url = EmbedVideoField()

class Mission_and_Vison(models.Model):
    mission = models.CharField(max_length=10000)
    vision = models.CharField(max_length=100000)


class ContactMessage(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone_number = models.CharField(max_length=25, null=True)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message from {self.name} ({self.email})"


class Manufacturing_and_Related_Service(models.Model):
    image = models.ImageField(upload_to='Services/Manufacturing_and_Related_Service/')

class Business_Registration_Consulting_Setup(models.Model):
    image = models.ImageField(upload_to='Services/Business_Registration_Consulting_Setup/')

class Media_and_Innovative_Designer(models.Model):
    image = models.ImageField(upload_to='Services/Media_and_Innovative_Designer/')

class Projects_and_Technical_Service(models.Model):
    image = models.ImageField(upload_to='Services/Projects_and_Technical_Service/')

class Travel_Support_Service(models.Model):
    image = models.ImageField(upload_to='Services/Travel_Support_Service/')