from django.urls import path
from . import views

urlpatterns = [
    # Add this to your existing URL patterns
    path('resend_otp/', views.resend_otp, name='resend_otp'),
] 