from django.shortcuts import render
from .models import Portfolio
from core.models import Person


def portfolio(request):

    projects = Portfolio.objects.all()
    person = Person.objects.first()


    return render(request, 'portfolio/portfolio.html', {
        'projects': projects,
        'person': person,
    })