import uuid



from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.



AGE_CHOICES = (
    ('All', 'All'),
    ('Kids', 'Kids')
) 
 
MOVIE_CHOICES = (
    ('Seasonal', 'Seasonal'),
    ('Casual', 'Casual')
)


class Profile(models.Model):
    name = models.CharField(max_length=255)
    age_limit = models.CharField(max_length=255, choices=AGE_CHOICES)
    uuid = models.UUIDField(default=uuid.uuid4)

    def __str__(self):
        return self.name



class CustomUser(AbstractUser):
    profiles = models.ManyToManyField(to=Profile, blank=True)

    def __str__(self):
        return self.username
    

class Video(models.Model):
    title = models.CharField(max_length=255, null=True, blank=True)
    file = models.FileField(upload_to='videoes')

    def __str__(self):
        return self.title


class Movie(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4)
    title = models.CharField(max_length=255)
    description = models.TextField()
    type = models.CharField(max_length=255, choices=MOVIE_CHOICES)      
    videos = models.ManyToManyField(Video)
    flyer = models.ImageField(upload_to='flyers')
    age_limit = models.CharField(max_length=255, choices=AGE_CHOICES)
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title