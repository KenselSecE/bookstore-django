from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
	path('book/<int:pk>/', views.book_detail, name='book_detail'),
	path('book/add/', views.add_book, name='add_book'),
	path('book/<int:pk>/edit/', views.edit_book, name='edit_book'),
	path('book/<int:pk>/delete/', views.delete_book, name='delete_book'),
	path('register/', views.register_view, name='register'),
	path('login/', views.login_view, name='login'),
	path('logout/', views.logout_view, name='logout'),
]