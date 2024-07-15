from django.urls import path
from app_main import views


urlpatterns = [
    path('', views.home, name='home'),
    path('login/google/', views.google_login, name='google_login'), # http://localhost:8000/login/google/
]


