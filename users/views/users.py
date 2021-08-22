#REST framework
from rest_framework import status, viewsets, mixins
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.generics import ListAPIView
from rest_framework.pagination import PageNumberPagination
from django.utils.translation import activate
from django.http import HttpResponseRedirect

#Permissions
from rest_framework.permissions import IsAuthenticated
from users.permissions import CheckProfileOwner

#Models
from django.contrib.auth.models import User
from django.shortcuts import render

#Serializer
from users.serializers.users import UserSerializer, NewUserSerializer
from users.serializers.signup import UserSignupSerializer
from users.serializers.verify import AccountVerificationSerializer

activate('es')

class UserListView (ListAPIView):
    """ List of all the users """
    queryset = User.objects.filter(is_staff=False)
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]
    pagination_class = None

class ProfileCompletionViewSet(mixins.UpdateModelMixin,
                              mixins.RetrieveModelMixin,
                              viewsets.GenericViewSet):
  ''' This is to complete the user data, in this moment it will only
      be used to post and patch the profile picture '''
  
  queryset = User.objects.all()
  serializer_class = UserSerializer
  permission_classes = [IsAuthenticated, CheckProfileOwner]

@api_view(['POST'])
def signup(request):
    if request.method == 'POST':
      serializer=UserSignupSerializer(data=request.data)
      serializer.is_valid(raise_exception=True)

      user=serializer.save()
      data=NewUserSerializer(user).data
      return Response(data)

@api_view(['GET'])
def account_verification(request, token):
    """ Account verification API view """

    if request.method == 'GET':
      token = request.path.split('/')
      token = token[3]
      data = {'token':f'{token}'}
      serializer = AccountVerificationSerializer(data=data)
      serializer.is_valid(raise_exception=True)
      serializer.save()
      data = {'message':'account verified successfully'}
      return HttpResponseRedirect('https://pedantic-panini-9d6199.netlify.app/verification')