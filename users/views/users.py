#REST framework
from rest_framework import status, viewsets, mixins
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.generics import ListAPIView
from rest_framework.pagination import PageNumberPagination

#Permissions
from rest_framework.permissions import IsAuthenticated

#Models
from django.contrib.auth.models import User

#Serializer
from users.serializers.users import UserSerializer, NewUserSerializer
from users.serializers.signup import UserSignupSerializer
from users.serializers.verify import AccountVerificationSerializer

@api_view(['POST'])
def signup(request):
    if request.method == 'POST':
      serializer=UserSignupSerializer(data=request.data)
      serializer.is_valid(raise_exception=True)

      user=serializer.save()
      data=NewUserSerializer(user).data
      return Response(data)

@api_view(['POST'])
def account_verification(request):
    """ Account verification API view """
    if request.method == 'POST':
      serializer = AccountVerificationSerializer(data=request.data)
      serializer.is_valid(raise_exception=True)
      serializer.save()
      data={'message':'Account verification success'}
      return Response(data,status=status.HTTP_200_OK)