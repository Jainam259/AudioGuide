STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
] 

# Email settings
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'  # Or your email provider's SMTP server
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'your-email@gmail.com'  # Replace with your email
EMAIL_HOST_PASSWORD = 'your-app-password'  # Use an app password for Gmail
DEFAULT_FROM_EMAIL = 'AudioGuide <your-email@gmail.com>'

# Twilio settings
TWILIO_ACCOUNT_SID = 'ACbe4704cd1911b9fe7556a7a4d340ec0e'
TWILIO_AUTH_TOKEN = '0e9f9054bcec3e76a423a41eeb49cfc0'
TWILIO_PHONE_NUMBER = '+17248748599'

# Add a flag to enable/disable Twilio in development
TWILIO_ENABLED = False if DEBUG else True 