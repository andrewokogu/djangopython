from django.shortcuts import render, HttpResponse
# Create your views here.


def test_view(request):
    return render(request, 'test.html')
    

def home_page(request):
    return HttpResponse("I am a new hompage!")
