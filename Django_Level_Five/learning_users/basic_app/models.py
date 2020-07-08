from django.db import models
from django.contrib.auth.models import User

# Create your models here.

def UserProfileInfo(models.Model):
    user = models.OneToOneField(User)

    portfolio = models.URLField(blank=True)
    picture = models.ImageField(upload_to='profile_pics')

    def __str__(self):
        return self.user.username