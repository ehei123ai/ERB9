from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def listings(request):
    return render(request, "listings/listings.html")

def listing(request, listing_id):
    return render(request, "listings/listing.html")