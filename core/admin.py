from django.contrib import admin


from .models import Profile, Video, Movie, CustomUser

# Register your models here.

admin.site.register(Profile)
admin.site.register(Video)
admin.site.register(Movie)
admin.site.register(CustomUser)