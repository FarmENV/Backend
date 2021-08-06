''' Account verification serializer '''

#Django
from django.conf import settings

#Django REST framework
from rest_framework import serializers

#Model
from django.contrib.auth.models import User

#Utilities
import jwt

class AccountVerificationSerializer(serializers.Serializer):
  ''' The account verification serializer '''

  token = serializers.CharField()

  def validate_token(self,data):
    ''' validates the token '''

    try:
      payload = jwt.decode(data, settings.SECRET_KEY, algorithms='HS256')
    except jwt.ExpiredSignatureError:
      raise serializers.ValidationError({'ERROR':'La verificación del link expiró'})
    except jwt.PyJWKError:
      raise serializers.ValidationError({'ERROR':'Token invalido'})

    if payload['type'] != 'email_confirmation':
      raise serializers.ValidationError({'ERROR':'Token invalido'})

    self.context['payload'] = payload

    return data

  def save(self):
    ''' Updates the user's verification status '''

    payload = self.context['payload']
    user = User.objects.get(username = payload['user'])
    user.profile.is_verified = True
    user.profile.save()
    return user