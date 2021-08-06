#Base User Admin config
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from django.contrib.auth.models import User
from users.models import Profile


class ProfileAdmin(admin.ModelAdmin):
    list_display = ['id','user']
    list_display_links = ['id','user']
    search_fields = ['user__email','user__is_staff','created_at','modified_at']
    list_filter = ['user__is_active','user__is_staff','created_at','modified_at']

class ProfileInline(admin.StackedInline):
    """ Profile in-line admin for users """
    model = Profile
    can_delete = False
    verbose_name_plural='profiles'

class UserAdmin(BaseUserAdmin):
    """ Add profile admin to base user admin """
    inlines = [ProfileInline]
    list_display = ['username','email','first_name','last_name','is_active','is_staff']
    list_editable = ['is_active','is_staff']

admin.site.unregister(User)
admin.site.register(User,UserAdmin)