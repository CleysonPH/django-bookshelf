from django.urls import path

from .views import review_create


app_name = 'reviews'
urlpatterns = [
    path('<int:book_pk>/nova/critica', review_create, name='review-create'),
]
