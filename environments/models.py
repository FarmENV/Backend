from django.db import models

# Create your models here.
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE

class Environment(models.Model):
  ''' The data for the environment '''

  farmer_id = models.ForeignKey(User, on_delete=models.CASCADE)
  arduino_id = models.CharField(max_length=100, blank = True, null = False,)
  environment_name = models.CharField(max_length=100, blank = True, null = False)
  environment_type = models.IntegerField()

  created_at = models.DateTimeField(auto_now = True)

  class Meta:
    ordering = ['created_at']

  def str(self):
    return self.environment_name
