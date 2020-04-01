from django.urls import path

from .views import ReviewList, ReviewUpdate, review_create


app_name = 'reviews'
urlpatterns = [
    path('<int:book_pk>/nova/critica', review_create, name='review-create'),
    path('criticas', ReviewList.as_view(), name='review-list'),
    path('critica/<int:pk>/editar', ReviewUpdate.as_view(), name='review-update'),
]
