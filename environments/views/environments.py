''' The environments ViewSet '''
from django.core import serializers

#REST framework
from rest_framework import viewsets, mixins
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.pagination import PageNumberPagination
from rest_framework.decorators import api_view
from rest_framework.views import APIView

# Models
from environments.models import Environment

# Serializer
from environments.serializers.environments import EnvModelSerializer
from environments.serializers.create import EnvironmentCreationSerializer
from environments.serializers.environments import NewEnvSerializer, EnvGetSerializer

class EnvViewSet(mixins.CreateModelMixin,
                   mixins.RetrieveModelMixin,
                   mixins.UpdateModelMixin,
                   mixins.DestroyModelMixin,
                   mixins.ListModelMixin,
                   viewsets.GenericViewSet):
  ''' Environments model ViewSet '''

  queryset = Environment.objects.all()
  serializer_class = EnvModelSerializer
  pagination_class = None

class EnvAPIView(APIView):
  
  def get(self,request,format=None):

    farmer_id = request.data['farmer_id']
    environments = serializers.serialize("json", Environment.objects.all().filter(farmer_id = farmer_id))
    
    data = EnvGetSerializer(environments).data
    print(environments)
    return Response(environments)


@api_view(['POST'])
def perform_create(request):
  ''' This saves the environment '''

  if request.method == 'POST':
    serializer = EnvironmentCreationSerializer(data = request.data)
    serializer.is_valid(raise_exception=True)

    environment = serializer.save()
    print(environment)
    data = NewEnvSerializer(environment).data
    return Response(data)

    
