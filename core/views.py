from django.shortcuts import render
from django.contrib.auth.models import User

from catalog.models import Book, Author
from reviews.models import Review


def home(request):
    context = {
        'page_title': 'Pratilheira Virtual',
        'page_description': 'Seja bem ao site Pratilheira Virtual sua rede social para leitores',
        'book_count': Book.objects.all().count(),
        'author_count': Author.objects.all().count(),
        'review_count': Review.objects.all().count(),
    }

    return render(request, 'core/home.html', context)
