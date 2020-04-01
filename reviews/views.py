from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required

from .forms import ReviewModelForm
from catalog.models import Book


@login_required
def review_create(request, book_pk):
    book = get_object_or_404(Book, pk=book_pk)

    if request.method == 'POST':
        form = ReviewModelForm(request.POST)
        review = form.save(commit=False)
        review.user = request.user
        review.book = book
        review.save()

        return redirect('catalog:book-detail', pk=book.pk)

    form = ReviewModelForm()
    context = {
        'page_title': 'Nova Crítica',
        'page_description': f'Faça uma crítica para o livro {book.title}',
        'form': form
    }

    return render(request, 'reviews/review_form.html', context)
