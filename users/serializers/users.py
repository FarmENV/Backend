# REST framework
from rest_framework import serializers

#Models
from django.contrib.auth.models import User
from users.models import Profile

class ProfileSerializer(serializers.ModelSerializer):
    """ Prifile model serializer """
    class Meta:
        model=Profile
        fields=['profile_picture']

class UserSerializer(serializers.ModelSerializer):
  ''' User model serializer '''

  profile = ProfileSerializer()

  class Meta:
    model=User
    fields=['id','username', 'email', 'first_name', 'last_name', 'profile']

  def update(self, instance, validated_data):

    profile_data = validated_data.pop('profile')
    profile = instance.profile

    instance.username = validated_data.get('username', instance.username)
    instance.first_name = validated_data.get('first_name', instance.first_name)
    instance.last_name = validated_data.get('last_name', instance.last_name)
    instance.email = validated_data.get('email', instance.email)
    instance.save()

    profile.profile_pic = profile_data.get('profile_pic', profile.profile_pic)
    profile.save()

    return instance

class NewUserSerializer(serializers.ModelSerializer):
  ''' It returns the new user data '''

  class Meta:
    model = User
    fields = ['username']