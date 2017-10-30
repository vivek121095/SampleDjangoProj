from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class UserProfileInfo(models.Model):

    #create relationship (don't inherit from User!)
    user = models.OneToOneField(User)

    #add extra attributes you want
    portfolio = models.URLField(blank=True)
    profilepicture = models.ImageField(upload_to='profile_pics',blank=True)

    def __str__(self):
        #Built in attributes of django.contrib.auth.models.User!
        return self.user.username
