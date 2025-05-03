from django.urls import path
from . import views

urlpatterns = [
    # ... existing URLs ...
    path('api/cities', views.cities_api, name='cities_api'),
] 