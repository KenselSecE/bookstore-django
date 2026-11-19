from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_routes, name='get_routes'),
    path('books/', views.get_books, name='get_books'),
    path('books/<int:pk>/', views.get_book, name='get_book'),
]