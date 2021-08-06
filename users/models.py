#Profile BaseUser Model
from django.db import models
from django.contrib.auth.models import User

class Profile (models.Model):
  ''' Data for the base user model '''

  user = models.OneToOneField(User,on_delete=models.CASCADE)
  profile_picture = models.ImageField(blank=True, null=True)
  
  is_verified = models.BooleanField(default=False)

  created_at = models.DateTimeField(auto_now=True)
  modified_at = models.DateTimeField(auto_now_add=True)

  class Meta:
    ordering = ['created_at']

  def __str__(self):
    return self.user.get_full_name()


 