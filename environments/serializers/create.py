#Django REST framework
from rest_framework import serializers
from rest_framework.validators import UniqueValidator

#Models
from django.contrib.auth.models import User
from environments.models import Environment

class EnvironmentCreationSerializer(serializers.Serializer):
  ''' This handles the creation of an environment '''

  username = serializers.CharField(min_length=3, max_length = 150, allow_blank = False)
  arduino_id = serializers.CharField(max_length=100, allow_blank = False, validators = [UniqueValidator(queryset=Environment.objects.all())])
  environment_name = serializers.CharField(max_length=100, allow_blank = False)
  environment_type = serializers.IntegerField()

  def create(self, data):

    farmer_id = User.objects.get(username = data['username'])

    environment = Environment.objects.create(farmer_id = farmer_id, 
                                            arduino_id = data['arduino_id'], 
                                            environment_name = data['environment_name'],
                                            environment_type = data['environment_type'])

    environment.save()

    return environment
