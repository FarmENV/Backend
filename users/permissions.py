''' Permissions to edit the user data '''

#REST framework
from rest_framework.permissions import BasePermission

#Models
from django.contrib.auth.models import User

class CheckProfileOwner(BasePermission):
  ''' This checks if the user who is trying to edit something
      is the owner of the account that is being edited '''

  def has_object_permission(self, request, view, obj):
      
      user_id = request.path.split('/')
      user_id = int(user_id[2])

      try:
        user = User.objects.get(username = request.user.username)
        if user.id == user_id:
          return True
      except User.DoesNotExist:
        return False