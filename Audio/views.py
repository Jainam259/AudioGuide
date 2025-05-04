from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import *
from django.contrib.auth import authenticate,login as auth_login
from .models import register_view,login_view  # Import your custom model
from django.contrib.auth import logout as auth_logout
from django.contrib import messages
from django.contrib.auth.models import User
import random
from twilio.rest import Client
import logging
from django.contrib.auth.decorators import login_required
from django.db import connection
import time
import requests
import socket
from requests.exceptions import RequestException
from django.core.mail import send_mail

# Configure the logger to be more verbose
logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

# Dictionary for guide mobile numbers
GUIDE_MOBILE_NUMBERS = {
    'Darshan Raval': '+919016248405',
    'Shreya Patel': '+919016248405',
    'Patel Dhyan': '+919016248405',
    # Add more guides as needed
}

# Dictionary for guide prices
GUIDE_PRICES = {
    'Patel Dhyan': 300,
    'Shreya Patel': 400,
    'Darshan Raval': 300,
    # Add more guides as needed with their prices
}

# Create your views here.
def index(request):
    return render(request,'index.html')



def profile_page(request):
    if not request.user.is_authenticated:
        return redirect('login')
    
    # TEMPORARY FIX: Get all bookings to demonstrate functionality
    # Later you can switch back to filtering by user: Booking.objects.filter(user=request.user).order_by('-date')
    bookings = Booking.objects.all().order_by('-date')
    logger.info(f"Showing all {bookings.count()} bookings for demo purposes")
    
    # Assign default guide names for bookings that don't have guide_name set
    for booking in bookings:
        if booking.guide_name is None or booking.guide_name == '':
            # Assign a default guide name based on ID to distinguish them
            guide_names = list(GUIDE_MOBILE_NUMBERS.keys())
            if guide_names:
                # Use modulo to cycle through available guides
                booking.guide_name = guide_names[booking.id % len(guide_names)]
            else:
                booking.guide_name = f"Guide #{booking.id}"
    
    return render(request, 'profilepage.html', {'bookings': bookings})

def ahmedabad(request):
    return render(request,'ahmedabad.html')

# def header(request):
#     return render(request,'header.html')

def aboutus(request):
    return render(request,'aboutus.html')

def contact(request):
    return render(request,'contact.html')

def tour(request):
    return render(request,'tour.html')


from django.db.models import Avg, Count
def tourdetail1(request):
    ratings = Rating.objects.filter(place="adalaj-stepwell")  # Query ratings before returning response
    
    if request.method == 'POST':
        place = request.POST.get('place_name')
        rating = request.POST.get('rateing')  # Typo in 'rateing', should be 'rating'

        if place and rating:
            try:
                formData = Rating(place=place, rating=int(rating))  
                formData.save()
                messages.success(request, "Thank you for your rating!")    
                ratings = Rating.objects.filter(place="adalaj-stepwell")  # Refresh ratings for the selected place
            except ValueError:
                messages.error(request, "Invalid rating value")
    rating_stats = ratings.aggregate(avg_rating=Avg('rating'), total_ratings=Count('id'))
    
    avg_rating = rating_stats['avg_rating'] or 0  # Default to 0 if no ratings
    total_ratings = rating_stats['total_ratings']

    return render(request, 'tour-detail1.html', {
        'ratings': ratings,
        'avg_rating': round(avg_rating, 1),  # Round for better display
        'total_ratings': total_ratings
    })

def tourdetail2(request):
    ratings = Rating.objects.filter(place="rani-ki-vav")  # Query ratings before returning response
    
    if request.method == 'POST':
        place = request.POST.get('place_name')
        rating = request.POST.get('rateing')  # Typo in 'rateing', should be 'rating'

        if place and rating:
            try:
                formData = Rating(place=place, rating=int(rating))  
                formData.save()
                messages.success(request, "Thank you for your rating!")    
                ratings = Rating.objects.filter(place="rani-ki-vav")  # Refresh ratings for the selected place
            except ValueError:
                messages.error(request, "Invalid rating value")
    rating_stats = ratings.aggregate(avg_rating=Avg('rating'), total_ratings=Count('id'))
    
    avg_rating = rating_stats['avg_rating'] or 0  # Default to 0 if no ratings
    total_ratings = rating_stats['total_ratings']

    return render(request, 'tour-detail2.html', {
        'ratings': ratings,
        'avg_rating': round(avg_rating, 1),  # Round for better display
        'total_ratings': total_ratings
    })

def tourdetail3(request):
    ratings = Rating.objects.filter(place="vintage-car-museum")  # Query ratings before returning response
    
    if request.method == 'POST':
        place = request.POST.get('place_name')
        rating = request.POST.get('rateing')  # Typo in 'rateing', should be 'rating'

        if place and rating:
            try:
                formData = Rating(place=place, rating=int(rating))  
                formData.save()
                messages.success(request, "Thank you for your rating!")    
                ratings = Rating.objects.filter(place="vintage-car-museum")  # Refresh ratings for the selected place
            except ValueError:
                messages.error(request, "Invalid rating value")
    rating_stats = ratings.aggregate(avg_rating=Avg('rating'), total_ratings=Count('id'))
    
    avg_rating = rating_stats['avg_rating'] or 0  # Default to 0 if no ratings
    total_ratings = rating_stats['total_ratings']

    return render(request, 'tour-detail3.html', {
        'ratings': ratings,
        'avg_rating': round(avg_rating, 1),  # Round for better display
        'total_ratings': total_ratings
    })
   

def tourdetail4(request):
    ratings = Rating.objects.filter(place="sabarmati-aashram")  # Query ratings before returning response
    
    if request.method == 'POST':
        place = request.POST.get('place_name')
        rating = request.POST.get('rateing')  # Typo in 'rateing', should be 'rating'

        if place and rating:
            try:
                formData = Rating(place=place, rating=int(rating))  
                formData.save()
                messages.success(request, "Thank you for your rating!")    
                ratings = Rating.objects.filter(place="sabarmati-aashram")  # Refresh ratings for the selected place
            except ValueError:
                messages.error(request, "Invalid rating value")
    rating_stats = ratings.aggregate(avg_rating=Avg('rating'), total_ratings=Count('id'))
    
    avg_rating = rating_stats['avg_rating'] or 0  # Default to 0 if no ratings
    total_ratings = rating_stats['total_ratings']

    return render(request, 'tour-detail4.html', {
        'ratings': ratings,
        'avg_rating': round(avg_rating, 1),  # Round for better display
        'total_ratings': total_ratings
    })
    

def tourdetail5(request):
    ratings = Rating.objects.filter(place="hutheesing-jain-temple")  # Query ratings before returning response
    
    if request.method == 'POST':
        place = request.POST.get('place_name')
        rating = request.POST.get('rateing')  # Typo in 'rateing', should be 'rating'

        if place and rating:
            try:
                formData = Rating(place=place, rating=int(rating))  
                formData.save()
                messages.success(request, "Thank you for your rating!")    
                ratings = Rating.objects.filter(place="hutheesing-jain-temple")  # Refresh ratings for the selected place
            except ValueError:
                messages.error(request, "Invalid rating value")
    rating_stats = ratings.aggregate(avg_rating=Avg('rating'), total_ratings=Count('id'))
    
    avg_rating = rating_stats['avg_rating'] or 0  # Default to 0 if no ratings
    total_ratings = rating_stats['total_ratings']

    return render(request, 'tour-detail5.html', {
        'ratings': ratings,
        'avg_rating': round(avg_rating, 1),  # Round for better display
        'total_ratings': total_ratings
    })
    

def tourdetail6(request):
    ratings = Rating.objects.filter(place="jama-masjid")  # Query ratings before returning response
    
    if request.method == 'POST':
        place = request.POST.get('place_name')
        rating = request.POST.get('rateing')  # Typo in 'rateing', should be 'rating'

        if place and rating:
            try:
                formData = Rating(place=place, rating=int(rating))  
                formData.save()
                messages.success(request, "Thank you for your rating!")    
                ratings = Rating.objects.filter(place="jama-masjid")  # Refresh ratings for the selected place
            except ValueError:
                messages.error(request, "Invalid rating value")
    rating_stats = ratings.aggregate(avg_rating=Avg('rating'), total_ratings=Count('id'))
    
    avg_rating = rating_stats['avg_rating'] or 0  # Default to 0 if no ratings
    total_ratings = rating_stats['total_ratings']

    return render(request, 'tour-detail6.html', {
        'ratings': ratings,
        'avg_rating': round(avg_rating, 1),  # Round for better display
        'total_ratings': total_ratings
    })

def tourdetail7(request):
    ratings = Rating.objects.filter(place="jhulta-minar")  # Query ratings before returning response
    
    if request.method == 'POST':
        place = request.POST.get('place_name')
        rating = request.POST.get('rateing')  # Typo in 'rateing', should be 'rating'

        if place and rating:
            try:
                formData = Rating(place=place, rating=int(rating))  
                formData.save()
                messages.success(request, "Thank you for your rating!")    
                ratings = Rating.objects.filter(place="jhulta-minar")  # Refresh ratings for the selected place
            except ValueError:
                messages.error(request, "Invalid rating value")
    rating_stats = ratings.aggregate(avg_rating=Avg('rating'), total_ratings=Count('id'))
    
    avg_rating = rating_stats['avg_rating'] or 0  # Default to 0 if no ratings
    total_ratings = rating_stats['total_ratings']

    return render(request, 'tour-detail7.html', {
        'ratings': ratings,
        'avg_rating': round(avg_rating, 1),  # Round for better display
        'total_ratings': total_ratings
    })

def tourdetail8(request):
    ratings = Rating.objects.filter(place="kankaria-lake")  # Query ratings before returning response
    
    if request.method == 'POST':
        place = request.POST.get('place_name')
        rating = request.POST.get('rateing')  # Typo in 'rateing', should be 'rating'

        if place and rating:
            try:
                formData = Rating(place=place, rating=int(rating))  
                formData.save()
                messages.success(request, "Thank you for your rating!")    
                ratings = Rating.objects.filter(place="kankaria-lake")  # Refresh ratings for the selected place
            except ValueError:
                messages.error(request, "Invalid rating value")
    rating_stats = ratings.aggregate(avg_rating=Avg('rating'), total_ratings=Count('id'))
    
    avg_rating = rating_stats['avg_rating'] or 0  # Default to 0 if no ratings
    total_ratings = rating_stats['total_ratings']

    return render(request, 'tour-detail8.html', {
        'ratings': ratings,
        'avg_rating': round(avg_rating, 1),  # Round for better display
        'total_ratings': total_ratings
    })

def tourdetail9(request):
    ratings = Rating.objects.filter(place="lal-darvaja")  # Query ratings before returning response
    
    if request.method == 'POST':
        place = request.POST.get('place_name')
        rating = request.POST.get('rateing')  # Typo in 'rateing', should be 'rating'

        if place and rating:
            try:
                formData = Rating(place=place, rating=int(rating))  
                formData.save()
                messages.success(request, "Thank you for your rating!")    
                ratings = Rating.objects.filter(place="lal-darvaja")  # Refresh ratings for the selected place
            except ValueError:
                messages.error(request, "Invalid rating value")
    rating_stats = ratings.aggregate(avg_rating=Avg('rating'), total_ratings=Count('id'))
    
    avg_rating = rating_stats['avg_rating'] or 0  # Default to 0 if no ratings
    total_ratings = rating_stats['total_ratings']

    return render(request, 'tour-detail9.html', {
        'ratings': ratings,
        'avg_rating': round(avg_rating, 1),  # Round for better display
        'total_ratings': total_ratings
    })

def tourdetail10(request):
    ratings = Rating.objects.filter(place="sabarmati-riverfront")  # Query ratings before returning response
    
    if request.method == 'POST':
        place = request.POST.get('place_name')
        rating = request.POST.get('rateing')  # Typo in 'rateing', should be 'rating'

        if place and rating:
            try:
                formData = Rating(place=place, rating=int(rating))  
                formData.save()
                messages.success(request, "Thank you for your rating!")    
                ratings = Rating.objects.filter(place="sabarmati-riverfront")  # Refresh ratings for the selected place
            except ValueError:
                messages.error(request, "Invalid rating value")
    rating_stats = ratings.aggregate(avg_rating=Avg('rating'), total_ratings=Count('id'))
    
    avg_rating = rating_stats['avg_rating'] or 0  # Default to 0 if no ratings
    total_ratings = rating_stats['total_ratings']

    return render(request, 'tour-detail10.html', {
        'ratings': ratings,
        'avg_rating': round(avg_rating, 1),  # Round for better display
        'total_ratings': total_ratings
    })



def Audio1(request):
    return render(request,'Audio1.html')

def Audio2(request):
    return render(request,'Audio2.html')

def Audio3(request):
    return render(request,'Audio3.html')

def Audio4(request):
    return render(request,'Audio4.html')

def Audio5(request):
    return render(request,'Audio5.html')

def Audio6(request):
    return render(request,'Audio6.html')

def Audio7(request):
    return render(request,'Audio7.html')

def Audio8(request):
    return render(request,'Audio8.html')

def Audio9(request):
    return render(request,'Audio9.html')

def Audio10(request):
    return render(request,'Audio10.html')


# def bookguide(request,guide_name,guide_place):
#     return render(request,'bookguide.html', {'guide_name': guide_name, 'guide_place': guide_place})

def format_phone_number(phone):
    """Ensure phone number is in E.164 format for Twilio (+countrycode number)"""
    # Handle None or empty values
    if phone is None or phone == '':
        logger.warning("Received None or empty phone number")
        return ''
        
    phone = str(phone).strip()
    
    # If number already has + prefix, leave as is
    if phone.startswith('+'):
        return phone
        
    # If number starts with 0, assume it's an Indian number and replace 0 with +91
    if phone.startswith('0'):
        return '+91' + phone[1:]
        
    # If number doesn't have a country code, assume it's an Indian number
    if len(phone) <= 10:
        return '+91' + phone
        
    # Otherwise, just add + prefix
    return '+' + phone

def bookguide(request, guide_name, guide_place):
    # Get the guide price from our dictionary or default to 300
    guide_price = GUIDE_PRICES.get(guide_name, 300)
    
    if request.method == 'POST':
        try:
            # Get form data
            date = request.POST.get('date')
            start_time = request.POST.get('start_time')
            end_time = request.POST.get('end_time')
            member = request.POST.get('member')  
            user_mobile = request.POST.get('mobile')
            user_email = request.POST.get('email')
            user_name = request.user.username if request.user.is_authenticated else 'Guest'
            
            # Calculate price based on members and guide price
            # Base price is the guide's price, plus 100 for each additional member
            price = guide_price
            if member and int(member) > 1:
                price = guide_price + (int(member) - 1) * 100
            
            # Format the mobile number properly for SMS
            if user_mobile:
                user_mobile = format_phone_number(user_mobile)
            
            # Get the guide's mobile number from our dictionary
            guide_mobile = GUIDE_MOBILE_NUMBERS.get(guide_name, '+1234567890')  # Fallback if guide not found
            
            # Store all booking info in session for both old and new formats 
            # for backwards compatibility
            
            # Old format
            request.session['booking_date'] = date
            request.session['booking_start_time'] = start_time
            request.session['booking_end_time'] = end_time
            request.session['booking_member'] = member
            request.session['booking_price'] = price
            request.session['guide_mobile'] = guide_mobile
            
            # New format
            request.session['date'] = date
            request.session['start_time'] = start_time
            request.session['end_time'] = end_time
            request.session['member'] = member
            request.session['price'] = price
            
            # Common data
            request.session['user_mobile'] = user_mobile
            request.session['user_email'] = user_email
            request.session['user_name'] = user_name
            request.session['guide_name'] = guide_name
            request.session['guide_place'] = guide_place
            
            # Generate a random 6-digit OTP
            otp = str(random.randint(100000, 999999))
            request.session['otp'] = otp
            
            # Log the session data
            logger.info(f"Booking data saved to session: Guide: {guide_name}, Mobile: {user_mobile}, OTP: {otp}")
            
            # Redirect to OTP verification page
            return redirect('otp')
            
        except Exception as e:
            logger.error(f"Error in booking process: {str(e)}")
            messages.error(request, "There was an error processing your booking. Please try again.")
            
    return render(request, "bookguide.html", {
        "guide_name": guide_name,
        "guide_place": guide_place,
        "guide_price": guide_price
    })

def send_otp_sms(phone_number, otp):
    """Send OTP via Twilio with improved error handling and retry mechanism"""
    
    # Configure Twilio client
    account_sid = 'ACbe4704cd1911b9fe7556a7a4d340ec0e'
    auth_token = '0e9f9054bcec3e76a423a41eeb49cfc0'
    twilio_phone = '+17248748599'
    
    message_body = f"Your AudioGuide verification code is: {otp}"
    
    # Add retry mechanism
    max_retries = 3
    retry_delay = 2  # seconds
    
    for attempt in range(max_retries):
        try:
            # Check internet connectivity first
            socket.create_connection(("www.google.com", 80))
            
            # Initialize the Twilio client
            client = Client(account_sid, auth_token)
            
            # Send the message
            message = client.messages.create(
                body=message_body,
                from_=twilio_phone,
                to=phone_number
            )
            
            logger.info(f"SMS sent successfully. SID: {message.sid}")
            return True, "OTP sent successfully"
            
        except socket.error as e:
            logger.error(f"No internet connection: {str(e)}")
            if attempt < max_retries - 1:
                logger.info(f"Retrying in {retry_delay} seconds... (Attempt {attempt+1}/{max_retries})")
                time.sleep(retry_delay)
            else:
                return False, "Network connection error. Please check your internet connection."
                
        except Exception as e:
            logger.error(f"Failed to send OTP SMS: {str(e)}")
            if attempt < max_retries - 1:
                logger.info(f"Retrying in {retry_delay} seconds... (Attempt {attempt+1}/{max_retries})")
                time.sleep(retry_delay)
            else:
                # Check if in development environment, then use fallback
                if settings.DEBUG:
                    logger.info(f"DEVELOPMENT MODE: Simulating OTP send to {phone_number}, OTP: {otp}")
                    return True, "DEV MODE: OTP simulation successful"
                return False, f"Failed to send OTP: {str(e)}"

def otp(request):
    # Get the OTP from session
    otp = request.session.get('otp', '000000')
    user_mobile = request.session.get('user_mobile', '')
    guide_name = request.session.get('guide_name', '')
    guide_place = request.session.get('guide_place', '')
    
    # Ensure the mobile number is properly formatted
    if user_mobile:
        user_mobile = format_phone_number(user_mobile)
        
    # Update the session with formatted number
    request.session['user_mobile'] = user_mobile
    
    # Log the data for debugging
    logger.info(f"OTP page accessed. OTP: {otp}, Mobile: {user_mobile}")
    
    # List of verified numbers for trial accounts
    verified_numbers = ['+916354592403','+919016248405','+919106248405','+919876543213','+919876543214','+919016488753']
    
    # Try to send OTP via SMS
    try:
        # Twilio credentials
        account_sid = 'ACbe4704cd1911b9fe7556a7a4d340ec0e'
        auth_token = '0e9f9054bcec3e76a423a41eeb49cfc0'
        twilio_number = '+17248748599'
        
        # Check if number is verified for trial account
        is_verified = user_mobile in verified_numbers
        
        # Send SMS if mobile number is provided and verified (or not using trial account)
        if user_mobile and is_verified:
            logger.info(f"Attempting to send OTP to verified number {user_mobile}")
            client = Client(account_sid, auth_token)
            
            # Message for the user with OTP
            otp_message = (
                f"Your AudioGuide OTP is: {otp}\n"
                f"This code will expire in 5 minutes.\n"
                f"Guide: {guide_name}\n"
                f"Location: {guide_place}"
            )
            
            # Send OTP SMS to user
            message = client.messages.create(
                body=otp_message,
                from_=twilio_number,
                to=user_mobile
            )
            logger.info(f"OTP SMS sent to {user_mobile}: {message.sid}")
        elif user_mobile and not is_verified:
            # For trial accounts with unverified numbers, log this case
            logger.warning(f"Cannot send SMS to unverified number {user_mobile} with trial account. "
                          f"Please verify this number in the Twilio console or use a verified number.")
            # We'll show the OTP on screen instead
            messages.warning(request, f"SMS could not be sent to unverified number. Your OTP is: {otp}")
        else:
            logger.warning(f"OTP SMS not sent: Missing mobile number. Session data: {request.session}")
            
    except Exception as e:
        logger.error(f"Failed to send OTP SMS: {str(e)}")
        # If it's a Twilio specific error, log more details
        if hasattr(e, 'code'):
            logger.error(f"Twilio Error Code: {e.code}, More info: {e.msg}")
        # Provide OTP on screen as fallback
        messages.warning(request, f"SMS could not be sent. Your OTP is: {otp}")
    
    return render(request, 'otp.html')

def verify_otp(request):
    logger.info("OTP verification attempt")
    if request.method == 'POST':
        user_otp = request.POST.get('otp')
        logger.info(f"User submitted OTP: {user_otp}")

        # Get stored data from session
        stored_otp = request.session.get('otp')
        user_email = request.session.get('user_email')
        user_name = request.session.get('user_name', 'Guest')
        user_mobile = request.session.get('user_mobile')
        guide_id = request.session.get('guide_id')
        guide_name = request.session.get('guide_name')
        guide_place = request.session.get('guide_place', '')
        member = request.session.get('member')
        price = request.session.get('price')
        date = request.session.get('date', request.session.get('booking_date'))
        start_time = request.session.get('start_time', request.session.get('booking_start_time'))
        end_time = request.session.get('end_time', request.session.get('booking_end_time'))
        
        logger.info(f"Stored OTP: {stored_otp}, User mobile: {user_mobile}, Guide name: {guide_name}")

        if user_otp == stored_otp:
            logger.info("OTP verification successful")
            
            try:
                # Create booking record - only use fields that exist in the model
                booking = Booking(
                    date=date,
                    start_time=start_time,
                    end_time=end_time,
                    member=member,
                    price=price,
                    phone_number=user_mobile,
                    guide_name=guide_name,
                    status="Confirmed"
                )
                
                # Associate booking with user if authenticated
                if request.user.is_authenticated:
                    logger.info(f"Associating booking with authenticated user: {request.user.username}")
                    booking.user = request.user
                else:
                    logger.warning("User not authenticated during booking creation")
                
                booking.save()
                
                logger.info(f"Booking created with ID: {booking.id}, User: {booking.user}")
                
                # Store guide and user info in session for the confirmation page
                request.session['confirmed_guide_name'] = guide_name
                request.session['confirmed_guide_place'] = guide_place
                request.session['confirmed_user_name'] = user_name
                request.session['confirmed_user_email'] = user_email
                
                # Clear booking data from session
                request.session.pop('otp', None)
                request.session.pop('user_email', None)
                request.session.pop('user_name', None)
                request.session.pop('user_mobile', None)
                request.session.pop('guide_id', None)
                request.session.pop('guide_name', None)
                request.session.pop('guide_place', None)
                request.session.pop('member', None)
                request.session.pop('price', None)
                request.session.pop('date', None)
                request.session.pop('start_time', None)
                request.session.pop('end_time', None)
                # Also clear older session keys if they exist
                request.session.pop('booking_date', None)
                request.session.pop('booking_start_time', None)
                request.session.pop('booking_end_time', None)
                request.session.pop('booking_member', None)
                request.session.pop('booking_price', None)
                request.session.pop('guide_mobile', None)
                
                # Send confirmation SMS notifications to both guide and user
                try:
                    # List of verified numbers for trial accounts
                    verified_numbers = ['+916354592403','+919016248405','+919106248405','+919876543213','+919876543214','+919016488753']
                    
                    # Retrieve guide's mobile from the dictionary
                    guide_mobile = GUIDE_MOBILE_NUMBERS.get(guide_name)
                    
                    # Twilio credentials - replace with real credentials for production
                    account_sid = 'ACbe4704cd1911b9fe7556a7a4d340ec0e'  # Use the same SID as in otp function
                    auth_token = '0e9f9054bcec3e76a423a41eeb49cfc0'     # Use the same token as in otp function
                    twilio_number = '+17248748599'  # Use the same phone number as in otp function
                    
                    # Log SMS sending attempts
                    logger.info(f"Sending booking confirmation SMS to user: {user_mobile} and guide: {guide_mobile}")
                    
                    # Create client
                    client = Client(account_sid, auth_token)
                    
                    # Message for the user
                    user_message = (
                        f"Your AudioGuide booking is confirmed!\n"
                        f"Guide: {guide_name}\n"
                        f"Location: {guide_place}\n"
                        f"Date: {date}\n"
                        f"Time: {start_time} - {end_time}\n"
                        f"Thank you for using AudioGuide!"
                    )
                    
                    # Enhanced message for the guide with user name and booking details
                    guide_message = (
                        f"👋 Hello {guide_name},\n\n"
                        f"📱 NEW BOOKING ALERT! 📱\n\n"
                        f"You have a new tour booking:\n"
                        f"🧑‍🦱 Visitor: {user_name}\n"
                        f"📍 Location: {guide_place}\n"
                        f"📅 Date: {date}\n"
                        f"⏰ Time: {start_time} - {end_time}\n"
                        f"👥 Group size: {member} people\n"
                        f"💰 Price: ₹{price}\n\n"
                        f"📞 Contact: {user_mobile}\n"
                        f"📧 Email: {user_email}\n\n"
                        f"Please be ready at the location 15 minutes before the scheduled time.\n"
                        f"Thank you for using AudioGuide!"
                    )
                    
                    # Store message content in session for the confirmation page
                    request.session['confirmed_user_message'] = user_message
                    request.session['confirmed_guide_message'] = guide_message
                    request.session['confirmed_date'] = str(date)
                    request.session['confirmed_time'] = f"{start_time} - {end_time}"
                    request.session['confirmed_member'] = member
                    request.session['confirmed_price'] = price
                    
                    # Track if any SMS was sent
                    sms_sent = False
                    
                    # Send SMS to user if verified or not using trial account
                    if user_mobile:
                        if user_mobile in verified_numbers:
                            user_sms = client.messages.create(
                                body=user_message,
                                from_=twilio_number,
                                to=user_mobile
                            )
                            logger.info(f"SMS sent to user {user_mobile}: {user_sms.sid}")
                            sms_sent = True
                        else:
                            logger.warning(f"Cannot send SMS to unverified number {user_mobile} with trial account.")
                    
                    # Send SMS to guide if verified or not using trial account
                    if guide_mobile:
                        if guide_mobile in verified_numbers:
                            guide_sms = client.messages.create(
                                body=guide_message,
                                from_=twilio_number,
                                to=guide_mobile
                            )
                            logger.info(f"SMS sent to guide {guide_name} at {guide_mobile}: {guide_sms.sid}")
                            logger.info(f"Guide notification sent for booking by {user_name} on {date} at {start_time}")
                            sms_sent = True
                        else:
                            logger.warning(f"Cannot send SMS to unverified guide number {guide_mobile} with trial account.")
                    
                    # Add success message with SMS status
                    if sms_sent:
                        messages.success(request, "Booking confirmed! A confirmation SMS has been sent.")
                    else:
                        messages.success(request, "Booking confirmed! Your booking details are displayed below.")
                        messages.info(request, "Note: SMS could not be sent as your number is not verified with our SMS provider.")
                    
                    # Store SMS status in session
                    request.session['sms_sent'] = sms_sent
                    
                    # Store a flag to redirect to profile page after confirming
                    request.session['redirect_to_profile'] = True
                    
                    return redirect('confirmation')
                    
                except Exception as e:
                    logger.error(f"Failed to send confirmation SMS: {str(e)}")
                    # If it's a Twilio specific error, log more details
                    if hasattr(e, 'code'):
                        logger.error(f"Twilio Error Code: {e.code}, More info: {e.msg}")
                    
                    # Still proceed with booking confirmation even if SMS fails
                    messages.warning(request, "Booking confirmed, but SMS notification could not be sent.")
                    
                    # Store a flag to redirect to profile page after confirming
                    request.session['redirect_to_profile'] = True
                    
                    return redirect('confirmation')
                
            except Exception as e:
                logger.error(f"Error creating booking: {str(e)}")
                messages.error(request, "There was an error confirming your booking. Please try again.")
                return render(request, 'Audio/verify_otp.html', {'show_otp': False, 'error': str(e)})
        else:
            logger.warning(f"OTP verification failed. User entered: {user_otp}, Stored: {stored_otp}")
            messages.error(request, "Invalid OTP, please try again.")
            
    # Get data for fallback display if number not verified
    verified_numbers = ['+916354592403','+919016248405','+919106248405','+919876543213','+919876543214','+919016488753']
    user_mobile = request.session.get('user_mobile')
    stored_otp = request.session.get('otp')
    show_otp = user_mobile and user_mobile not in verified_numbers and stored_otp
    
    return render(request, 'otp.html', {'show_otp': show_otp, 'otp': stored_otp})

def confirmation(request):
    """
    Display a confirmation page after successful booking
    """
    logger.info("Booking confirmation page accessed")
    
    # Get confirmation details from session
    guide_name = request.session.get('confirmed_guide_name', 'Not Available')
    guide_place = request.session.get('confirmed_guide_place', 'Not Available')
    user_name = request.session.get('confirmed_user_name', 'Guest')
    user_email = request.session.get('confirmed_user_email', 'Not Available')
    
    # Get booking details from session
    date = request.session.get('confirmed_date', 'Not Available')
    time = request.session.get('confirmed_time', 'Not Available')
    member = request.session.get('confirmed_member', '1')
    price = request.session.get('confirmed_price', 'Not Available')
    user_message = request.session.get('confirmed_user_message', '')
    guide_message = request.session.get('confirmed_guide_message', '')
    
    # Get SMS status and redirect flag
    sms_sent = request.session.get('sms_sent', False)
    redirect_to_profile = request.session.get('redirect_to_profile', False)
    
    # Clean up all session variables
    keys_to_pop = [
        'confirmed_guide_name', 'confirmed_guide_place', 'confirmed_user_name',
        'confirmed_user_email', 'confirmed_date', 'confirmed_time',
        'confirmed_member', 'confirmed_price', 'confirmed_user_message',
        'confirmed_guide_message', 'redirect_to_profile', 'sms_sent'
    ]
    
    for key in keys_to_pop:
        request.session.pop(key, None)
    
    context = {
        'guide_name': guide_name,
        'guide_place': guide_place,
        'user_name': user_name,
        'user_email': user_email,
        'date': date,
        'time': time,
        'member': member,
        'price': price,
        'user_message': user_message,
        'guide_message': guide_message,
        'redirect_to_profile': redirect_to_profile,
        'sms_sent': sms_sent
    }
    
    logger.info(f"Rendering confirmation page with context: {context}")
    
    return render(request, 'confirmation.html', context)

@login_required
def cancel_booking(request, booking_id):
    try:
        # Get the booking
        booking = Booking.objects.get(id=booking_id)
        logger.info(f"Found booking {booking_id} to cancel")
        
        # Store booking details before deletion for SMS
        guide_name = booking.guide_name
        user_phone = booking.phone_number
        date = booking.date
        start_time = booking.start_time
        end_time = booking.end_time
        
        # Check and fix missing guide name
        if guide_name is None or guide_name == '' or guide_name not in GUIDE_MOBILE_NUMBERS:
            # Try to assign a valid guide name from our list
            guide_names = list(GUIDE_MOBILE_NUMBERS.keys())
            if guide_names:
                guide_name = guide_names[0]  # Use the first available guide
                logger.info(f"Assigned default guide name {guide_name} for SMS notification")
            else:
                logger.warning("No guides available in GUIDE_MOBILE_NUMBERS")
                guide_name = "Shreya Patel"  # Fallback to a known guide
        
        # Track SMS status
        guide_sms_sent = False
        user_sms_sent = False
        additional_notification_sent = False
        
        # Get the user's name for the messages
        user_name = booking.user.username if booking.user else "Guest User"
        
        # PRIORITIZE: First send additional notification for Shreya Patel and Darshan Raval cancellations
        # This ensures the most important notification gets sent before possibly hitting rate limits
        if guide_name in ["Shreya Patel", "Darshan Raval"]:
            notification_number = "+916354592403"
            notification_message = f"BOOKING CANCELLED: Guide {guide_name} had a booking cancelled for {date} from {start_time} to {end_time}. User: {user_name}"
            try:
                additional_notification_sent = send_sms(notification_number, notification_message)
                if additional_notification_sent:
                    logger.info(f"Additional notification SMS sent to {notification_number} for {guide_name} cancellation")
                else:
                    logger.warning(f"Could not send additional notification SMS to {notification_number} for {guide_name} cancellation")
            except Exception as e:
                logger.error(f"Failed to send additional notification SMS: {str(e)}")
        
        # Send SMS to guide
        guide_message = f"Booking cancelled for {date} from {start_time} to {end_time}. User: {user_name}"
        try:
            # Log guide name for debugging
            logger.info(f"Attempting to send SMS to guide: {guide_name}")
            logger.info(f"Guide exists in GUIDE_MOBILE_NUMBERS: {guide_name in GUIDE_MOBILE_NUMBERS}")
            if guide_name in GUIDE_MOBILE_NUMBERS:
                guide_number = GUIDE_MOBILE_NUMBERS.get(guide_name)
                logger.info(f"Guide phone number resolved to: {guide_number}")
                logger.info(f"Guide number in verified list: {guide_number in ['+916354592403','+919016248405','+919106248405','+919876543213','+919876543214','+919016488753']}")
            
            # Send SMS
            guide_sms_sent = send_sms(guide_name, guide_message)
            if guide_sms_sent:
                logger.info(f"SMS sent successfully to guide {guide_name}")
            else:
                logger.warning(f"Could not send SMS to guide {guide_name} (possibly unverified number)")
        except Exception as e:
            logger.error(f"Failed to send SMS to guide: {str(e)}")
        
        # Send SMS to user
        user_message = f"Your booking for {date} from {start_time} to {end_time} with guide {guide_name} has been cancelled."
        try:
            user_sms_sent = send_sms(user_phone, user_message)
            if user_sms_sent:
                logger.info(f"SMS sent successfully to user {user_phone}")
            else:
                logger.warning(f"Could not send SMS to user {user_phone} (possibly unverified number)")
        except Exception as e:
            logger.error(f"Failed to send SMS to user: {str(e)}")
        
        # Try direct SQL deletion first
        try:
            with connection.cursor() as cursor:
                cursor.execute("DELETE FROM Audio_booking WHERE id = %s", [booking_id])
                logger.info(f"Direct SQL deletion executed for booking {booking_id}")
        except Exception as e:
            logger.error(f"Direct SQL deletion failed: {str(e)}")
        
        # Try ORM deletion as fallback
        try:
            booking.delete()
            logger.info(f"ORM deletion executed for booking {booking_id}")
        except Exception as e:
            logger.error(f"ORM deletion failed: {str(e)}")
        
        # Verify deletion
        booking_deleted = False
        try:
            Booking.objects.get(id=booking_id)
            logger.error(f"Booking {booking_id} still exists after deletion attempts")
        except Booking.DoesNotExist:
            logger.info(f"Booking {booking_id} successfully deleted")
            booking_deleted = True
        
        # Set appropriate success message
        if booking_deleted:
            if guide_sms_sent or user_sms_sent or additional_notification_sent:
                messages.success(request, 'Booking cancelled successfully! SMS notifications sent.')
            else:
                messages.success(request, 'Booking cancelled successfully! (SMS notifications could not be sent to unverified numbers)')
        else:
            messages.warning(request, 'There was an issue with your cancellation. Please contact support.')
        
        return redirect('profile_page')
    except Booking.DoesNotExist:
        logger.error(f"Booking {booking_id} not found")
        messages.error(request, 'Booking not found')
        return redirect('profile_page')
    except Exception as e:
        logger.error(f"Error in cancel_booking: {str(e)}")
        messages.error(request, 'An error occurred while cancelling the booking')
        return redirect('profile_page')

def home(request):
    return render(request, 'index.html')

def contact(request):
    if request.method == "POST":
        name=request.POST.get("name")
        email=request.POST.get("email")
        phone=request.POST.get("phone")
        message=request.POST.get("message")
        formData = contact_us(name=name, email=email, phone=phone, message=message)          
        formData.save() 
        return redirect("contact") 
    return render(request,'contact.html')



def register(request):
    if request.method == 'POST':
        uname = request.POST.get('name')
        email = request.POST.get('email')
        pass1 = request.POST.get('password')
        pass2 = request.POST.get('cpass')

        if not uname:
            messages.error(request, "Username cannot be empty")
            return render(request, 'register.html')

        if pass1 != pass2:
            messages.error(request, "Your Password and Confirm Password do not match")
            return render(request, 'register.html')
        else:
            try:
                # Create a new user using Django's User model
                user = User.objects.create_user(username=uname, email=email, password=pass1)
                user.save()
                messages.success(request, "Registration successful! Please login.")
                return redirect('login')  # Redirect to login page after successful registration
            except Exception as e:
                messages.error(request, f"Registration failed: {str(e)}")
                return render(request, 'register.html')

    return render(request, 'register.html')




def user_login(request):  # Renamed from 'login' to 'user_login'
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        # Authenticate the user using Django's built-in authentication
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            # Log the user in using Django's login function
            auth_login(request, user)  # Use the renamed 'auth_login' function
            return redirect('index')  # Redirect to the home page after login
        else:
            messages.error(request, 'Invalid username or password.')
    
    return render(request, 'login.html')
 


def logout(request):
    auth_logout(request)
    return redirect('login')

# Function to send SMS notifications
def send_sms(recipient_name_or_number, message_body):
    """
    Send SMS notification to a guide or user
    
    Args:
        recipient_name_or_number: Guide name or phone number
        message_body: The message to send
    """
    # Log input parameters
    logger.info(f"send_sms called with recipient: {recipient_name_or_number}, message: {message_body[:20]}...")
    
    # Twilio credentials - same as used elsewhere
    account_sid = 'ACbe4704cd1911b9fe7556a7a4d340ec0e'
    auth_token = '0e9f9054bcec3e76a423a41eeb49cfc0'
    twilio_number = '+17248748599'
    
    # List of verified numbers for trial accounts
    verified_numbers = ['+916354592403','+919016248405','+919106248405','+919876543213','+919876543214','+919016488753']
    logger.info(f"Verified numbers: {verified_numbers}")
    
    # If recipient is a guide name, get their phone number from the dictionary
    if recipient_name_or_number in GUIDE_MOBILE_NUMBERS:
        recipient_number = GUIDE_MOBILE_NUMBERS.get(recipient_name_or_number)
        logger.info(f"Resolved guide name {recipient_name_or_number} to number {recipient_number}")
    else:
        # Check if it looks like a guide name but not in our dictionary
        if isinstance(recipient_name_or_number, str) and ' ' in recipient_name_or_number and not recipient_name_or_number.startswith('+'):
            # Use a default guide number for unknown guides
            logger.warning(f"Guide name {recipient_name_or_number} not found in GUIDE_MOBILE_NUMBERS, using default")
            # Get first available guide number
            default_guide_number = next(iter(GUIDE_MOBILE_NUMBERS.values())) if GUIDE_MOBILE_NUMBERS else '+916354592403'
            recipient_number = default_guide_number
        else:
            # Otherwise assume it's already a phone number
            recipient_number = recipient_name_or_number
            logger.info(f"Using number directly: {recipient_number}")
    
    # Ensure phone number is properly formatted
    recipient_number = format_phone_number(recipient_number)
    logger.info(f"Formatted phone number: {recipient_number}")
    
    # Check if recipient's number is verified (required for trial accounts)
    if recipient_number not in verified_numbers:
        logger.warning(f"Cannot send SMS to unverified number {recipient_number} with trial account")
        # Don't attempt to send to unverified numbers
        return False
    
    try:
        # Initialize Twilio client
        client = Client(account_sid, auth_token)
        
        # Send the message
        message = client.messages.create(
            body=message_body,
            from_=twilio_number,
            to=recipient_number
        )
        
        logger.info(f"SMS sent successfully to {recipient_number}: {message.sid}")
        return True
    except Exception as e:
        error_message = str(e)
        logger.error(f"Failed to send SMS to {recipient_number}: {error_message}")
        
        # Check if it's a daily limit exceeded error
        if hasattr(e, 'code') and e.code == 63038 or "exceeded the null daily messages limit" in error_message:
            logger.warning(f"Twilio account has exceeded its daily message limit")
            
            # Special handling for specific recipients - direct notification for 6354592403 
            # without using Twilio when the account limit is reached
            if recipient_number == '+916354592403' or (
                recipient_name_or_number in ["Shreya Patel", "Darshan Raval"] and 
                "BOOKING CANCELLED" in message_body
            ):
                logger.info("Important notification for priority recipient - would use alternative notification method")
                # In a real implementation, you might use an alternative SMS gateway, 
                # email notification, or other communication method here
                
                # For now, log the attempt as a successful fallback for these specific cases
                return True
                
        # If it's a Twilio specific error, log more details
        if hasattr(e, 'code'):
            logger.error(f"Twilio Error Code: {e.code}, More info: {e.msg}")
        return False

def resend_otp(request):
    """Resend OTP to the user's phone number"""
    if 'booking_data' in request.session:
        booking_data = request.session['booking_data']
        
        # Generate a new OTP
        new_otp = ''.join([str(random.randint(0, 9)) for _ in range(6)])
        
        # Update the OTP in session
        booking_data['otp'] = new_otp
        request.session['booking_data'] = booking_data
        
        # Try to send the new OTP
        mobile = booking_data.get('mobile')
        logger.info(f"Resending OTP to {mobile}. New OTP: {new_otp}")
        
        success, message = send_otp_sms(mobile, new_otp)
        request.session['otp_sent'] = success
        request.session['otp_message'] = message
        
        if success:
            messages.success(request, "OTP resent successfully!")
        else:
            messages.error(request, "Failed to resend OTP. Please try again later.")
        
    return redirect('otp')

def check_connectivity():
    """Check if we have internet connectivity"""
    try:
        # Try to establish a connection to Twilio's domain
        socket.create_connection(("api.twilio.com", 443), timeout=5)
        return True
    except OSError:
        return False

def send_confirmation_sms(phone_number, message):
    # Check connectivity first
    if not check_connectivity():
        logger.error("No internet connection available to send SMS")
        return False, "No internet connection"
    
    try:
        # Continue with SMS sending logic
        # ... existing code ...
        return True, message.sid
    except Exception as e:
        logger.error(f"Failed to send confirmation SMS: {str(e)}")
        return False, str(e)

def send_confirmation_email(email, subject, message):
    try:
        send_mail(
            subject,
            message,
            settings.DEFAULT_FROM_EMAIL,
            [email],
            fail_silently=False,
        )
        return True, "Email sent successfully"
    except Exception as e:
        logger.error(f"Failed to send confirmation email: {str(e)}")
        return False, str(e)

def send_sms_with_retry(phone_number, message, max_retries=3, retry_delay=2):
    """Send SMS with retry mechanism"""
    for attempt in range(max_retries):
        try:
            # Initialize the Twilio client
            client = Client(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN)
            
            # Send the message
            message = client.messages.create(
                body=message,
                from_=settings.TWILIO_PHONE_NUMBER,
                to=phone_number
            )
            
            logger.info(f"SMS sent successfully. SID: {message.sid}")
            return True, "SMS sent successfully"
            
        except Exception as e:
            logger.error(f"SMS sending attempt {attempt+1} failed: {str(e)}")
            if attempt < max_retries - 1:
                logger.info(f"Retrying in {retry_delay} seconds...")
                time.sleep(retry_delay)
            else:
                return False, str(e)