from django.shortcuts import render

# Create your views here.
def my_first_view(request):
    return render(request, 'testing/testing.html')