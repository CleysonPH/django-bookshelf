from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

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


class ReviewUpdate(UpdateView, LoginRequiredMixin):
    model = Review
    form_class = ReviewModelForm
    success_url = reverse_lazy('reviews:review-list')

    def get_object(self):
        return get_object_or_404(Review, pk=self.kwargs.get('pk'), user=self.request.user)

    def get_context_data(self, **kwargs):
        context = super(ReviewUpdate, self).get_context_data(**kwargs)
        context['page_title'] = 'Editar Crítica'
        context['page_description'] = f'Edite aqui a crítica "{context["review"].title}"'
        return context
