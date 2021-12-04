from django.shortcuts import render
from django.http import HttpResponse
from .models import Feature


def index(request):
    feature1 = Feature()
    feature1.id = 0
    feature1.name = 'Fast'
    feature1.details = 'Our service is very quick.'
    feature1.is_true = True

    feature2 = Feature()
    feature2.id = 1
    feature2.name = 'Reliable'
    feature2.details = 'Our service is very realiable.'
    feature2.is_true = True

    feature3 = Feature()
    feature3.id = 2
    feature3.name = 'Easy'
    feature3.details = 'Our service is very easy.'
    feature3.is_true = False

    feature4 = Feature()
    feature4.id = 3
    feature4.name = 'Affordable'
    feature4.details = 'Our service is very affordable.'
    feature4.is_true = True

    feature5 = Feature()
    feature5.id = 4
    feature5.name = 'feature 5'
    feature5.details = 'Our service is very feature 5.'
    feature5.is_true = True

    features = [feature1, feature2, feature3, feature4, feature5]

    return render(request, 'index.html', {'features': features})


def counter(request):
    text = request.POST['text']
    amount_of_words = len(text.split())
    return render(request, 'counter.html', {'amount': amount_of_words})
