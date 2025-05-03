from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import City

@csrf_exempt
def cities_api(request):
    """API endpoint to manage cities - GET only"""
    if request.method == 'GET':
        # Get all cities
        try:
            cities = City.objects.all()
            cities_data = list(cities.values('id', 'name', 'country', 'population', 'description'))
            return JsonResponse(cities_data, safe=False)
        except Exception as e:
            return JsonResponse({'message': str(e)}, status=500)
    
    # Method not allowed - POST is no longer supported
    return JsonResponse({'message': 'Method not allowed'}, status=405) 