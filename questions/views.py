from django.shortcuts import render, HttpResponseRedirect
from questions.models import *


def index(request):
    categories = Category.objects.all()
    context = {

        "categories": categories
    }
    return render(request, 'categories.html', context)


def category(request):
    cat = request.get_host().split('.')[0]
    try:
        category = Category.objects.get(slug=cat)
        questions = Question.objects.filter(category=category)

        context = {
            'questions': questions
        }
        return render(request, 'category.html', context)
    except:
        return HttpResponseRedirect('http://www.localhost:8000/')
