from django.shortcuts import render

from unique_offer_screen.models import UniqueOffer, OurProsBlock


# Create your views here.

def main_page_render(request):
    offer = UniqueOffer.objects.first()
    pros = OurProsBlock.objects.all()
    return render(request, 'main_page/main_page.html', {'offer': offer, "pros": pros})