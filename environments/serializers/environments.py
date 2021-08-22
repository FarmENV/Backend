''' The environments model serializer '''

#REST framework
from django.contrib.auth import models
from django.db.models import fields
from rest_framework import serializers

#Models
from django.contrib.auth.models import User
from environments.models import Environment

class EnvModelSerializer(serializers.ModelSerializer):
  ''' Environment model serializer '''

  class Meta:
    model = Environment
    fields = ['id','farmer_id', 'arduino_id','environment_name', 'environment_type', 'created_at']

class NewEnvSerializer(serializers.ModelSerializer):
  ''' It returns the new env data '''

  class Meta:
    model = Environment
    fields = ['arduino_id']

class EnvGetSerializer(serializers.ModelSerializer):
  ''' It returns the new env data '''

  class Meta:
    model = Environment
    fields = ['environment_name']
