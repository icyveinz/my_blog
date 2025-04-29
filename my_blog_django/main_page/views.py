from django.shortcuts import render

from unique_offer_screen.models import UniqueOffer


# Create your views here.

def main_page_render(request):
    offer = UniqueOffer.objects.first()
    if offer:
        print(f"Offer found: {offer.title}")
    else:
        print("No offer found")
    return render(request, 'main_page/main_page.html', {'offer': offer})