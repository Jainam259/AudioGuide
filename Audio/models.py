from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class register_view(models.Model):
    name = models.CharField(max_length=100, null=True)
    email = models.EmailField(max_length=50)  # Changed to EmailField for validation
    password = models.CharField(max_length=255)  # Increased length for better security
    cpass = models.CharField(max_length=255)  # Increased length for consistency

    def __str__(self):
        return self.name
    
class login_view(models.Model):
    name=models.CharField(max_length=100,null=True)
    password=models.CharField(max_length=8)
        

class contact_us(models.Model):
    name=models.CharField(max_length=100,null=True)
    email=models.CharField(max_length=50)
    phone = models.CharField(max_length=15)
    message=models.CharField(max_length=500)


class Booking(models.Model):
    STATUS_CHOICES = [
        ('Confirmed', 'Confirmed'),
        ('Cancelled', 'Cancelled'),
    ]
    
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    guide_name = models.CharField(max_length=100, null=True, blank=True)
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    member = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    phone_number = models.CharField(max_length=15, null=True, blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Confirmed')
    
    def __str__(self):
        return f"Booking on {self.date} from {self.start_time} to {self.end_time}"
        
    def get_mobile(self):
        """Get the mobile number regardless of field name"""
        if hasattr(self, 'phone_number'):
            return self.phone_number
        if hasattr(self, 'mobile'):
            return self.mobile
        return None
        
    def set_mobile(self, number):
        """Set the mobile number to the appropriate field"""
        if hasattr(self, 'phone_number'):
            self.phone_number = number
        elif hasattr(self, 'mobile'):
            self.mobile = number


class Rating(models.Model):
    PLACE_CHOICES = [
        ("adalaj-stepwell", "Adalaj Stepwell"),
        ("rani-ki-vav", "Rani Ki Vav"),
        ("vintage-car-museum", "The Vintage Car Museum"),
        ("sabarmati-aashram", "Sabarmati Aashram"),
        ("hutheesing-jain-temple", "Hutheesing Jain Temple"),
        ("jama-masjid", "Jama Masjid"),
        ("jhulta-minar", "Jhulta Minar"),
        ("kankaria-lake", "Kankaria Lake"),
        ("lal-darvaja", "Lal Darvaja"),
        ("sabarmati-riverfront", "Sabarmati Riverfront"),
    ]

    place = models.CharField(max_length=50, choices=PLACE_CHOICES)
    rating = models.IntegerField()

    def _str_(self):
        return f"{self.get_place_display()} - {self.rating}/10"

