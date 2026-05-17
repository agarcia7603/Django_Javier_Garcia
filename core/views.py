from django.shortcuts import render, HttpResponse
from .models import Person

# Create your views here.
def home(request):

    person = Person.objects.first()

    return render(request, 'core/home.html', {
        'person': person
    })

def about(request):
    person = Person.objects.first()
    return render(request, "core/about.html", {
        'person': person
    })

def portfolio(request):
    person = Person.objects.first()
    return render(request, "core/../portfolio/templates/portfolio/portfolio.html", {
        'person': person
    })

def contact(request):
    person = Person.objects.first()
    return render(request, "core/contact.html", {
        'person': person
    })