from django.contrib import admin

''' Admin configuration for environments '''

from django.contrib import admin

#Models
from environments.models import Environment

@admin.register(Environment)
class EnvironmentAdmin(admin.ModelAdmin):
  list_display = ['arduino_id', 'environment_name', 'environment_type', 'farmer_id']
  search_fields = ['arduino_id', 'farmer_id']
  list_filter = ['created_at']
