from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import ReviewModelForm
from .models import Review
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


class ReviewList(ListView, LoginRequiredMixin):
    model = Review

    def get_queryset(self):
        return Review.objects.filter(user=self.request.user)

    def get_context_data(self, **kwargs):
        context = super(ReviewList, self).get_context_data(**kwargs)
        context['page_title'] = 'Críticas'
        context['page_description'] = 'Todos as críticas realizadas por você'
        return context
