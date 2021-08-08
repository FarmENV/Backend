from django.contrib import admin
from django.db import router
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

from users.views import users as users_views
from users.views.login import UserLoginAPIView as login
from users.views.users import ProfileCompletionViewSet
from environments.views import environments as environments_views

#Django REST framework
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'profile', ProfileCompletionViewSet, basename = 'profile')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', users_views.UserListView.as_view(), name='users'),
    path('users/signup/', users_views.signup, name='signup'),
    path('users/verify/', users_views.account_verification, name='verify'),
    path('users/login/', login.as_view(), name='login'),
    path('environments/create/',environments_views.perform_create, name='create'),
    path('', include(router.urls))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

