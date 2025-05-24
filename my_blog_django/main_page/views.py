from django.shortcuts import render

from main_page.blog.models import Article
from main_page.stack_element.models import SquareCard
from main_page.unique_offer_screen.models import UniqueOffer, OurProsBlock


# Create your views here.

def main_page_render(request):
    offer = UniqueOffer.objects.first()
    pros = OurProsBlock.objects.all()
    top_three_articles = Article.objects.all()[:3]
    stack_cards = SquareCard.objects.all()
    return render(request, 'main_page/main_page.html',
                  {
                      'offer': offer,
                      "pros": pros,
                      "top_three_articles": top_three_articles,
                      "stack_cards": stack_cards,
                  })