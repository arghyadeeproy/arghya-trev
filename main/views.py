from django.http import HttpResponse
from django.shortcuts import render
from .models import Hotels
from django.db.models import Q

def home(request):
    return render(request, 'main/index.html')

def listing(request):
    # Get place from URL parameter, default to "puri"
    place_name = request.GET.get('place', 'puri')
    
    # Start with hotels from the selected place
    hotels = Hotels.objects.filter(place_name__iexact=place_name)
    
    # Get filter parameters from URL
    property_types = request.GET.getlist('property_type')
    max_price = request.GET.get('max_price')
    
    # Apply property type filters
    if property_types:
        hotels = hotels.filter(property_type__in=property_types)
    
    # Apply price filter
    if max_price:
        try:
            max_price = float(max_price)
            hotels = hotels.filter(price__lte=max_price)
        except ValueError:
            pass
    
    # Get counts for each filter option (for display in sidebar)
    all_hotels = Hotels.objects.filter(place_name__iexact=place_name)
    
    filter_counts = {
        'House': all_hotels.filter(property_type='House').count(),
        'Hostel': all_hotels.filter(property_type='Hostel').count(),
        'Flat': all_hotels.filter(property_type='Flat').count(),
        'Villa': all_hotels.filter(property_type='Villa').count(),
        'GuestSuite': all_hotels.filter(property_type='Guest-Suite').count(),
        'price_50': all_hotels.filter(price__lte=50).count(),
        'price_60': all_hotels.filter(price__lte=60).count(),
        'price_70': all_hotels.filter(price__lte=70).count(),
        'price_80': all_hotels.filter(price__lte=80).count(),
        'price_90': all_hotels.filter(price__lte=90).count(),
        'price_100': all_hotels.filter(price__lte=100).count(),
        'price_100_plus': all_hotels.filter(price__gt=100).count(),
    }
    
    context = {
        'hotels': hotels,
        'filter_counts': filter_counts,
        'selected_property_types': property_types,
        'selected_max_price': max_price,
        'total_count': hotels.count(),
        'place_name': place_name.title(),  # Capitalize for display
        'place_param': place_name  # Keep original for URL params
    }
    
    return render(request, 'main/listing.html', context)

def hotel(request):
    hotel_id = request.GET.get('hotel')
    if hotel_id:
        try:
            hotel = Hotels.objects.get(id=hotel_id)
            return render(request, 'main/hotel.html', {'hotel': hotel})
        except Hotels.DoesNotExist:
            return HttpResponse("Hotel not found")
    return HttpResponse("Waiting....")

def payment(request):
    return HttpResponse("Awaitingg.....")
def login(request):
    return HttpResponse("Waiting....")