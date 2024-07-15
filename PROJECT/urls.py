from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('app_main.urls')),
    path('social-auth/',include('social_django.urls', namespace='social')),
    path('users/', include('app_users.urls')),

]
