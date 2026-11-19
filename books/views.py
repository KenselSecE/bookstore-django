from django.shortcuts import render
from .models import Book
from django.shortcuts import get_object_or_404, redirect
from .forms import BookForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from .forms import RegisterForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden

def homepage(request):
    books = Book.objects.all()
    context = {'books': books}
    return render(request, 'books/homepage.html', context)

def book_detail(request, pk):
    book = get_object_or_404(Book, pk=pk)
    context = {'book': book}
    return render(request, 'books/book_detail.html', context)

@login_required
def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            book = form.save(commit=False)
            book.posted_by = request.user
            book.save()
            return redirect('homepage')
    else:
        form = BookForm()

    context = {'form': form}
    return render(request, 'books/add_book.html', context)

@login_required
def edit_book(request, pk):
    book = get_object_or_404(Book, pk=pk)

    if book.posted_by != request.user:
        return HttpResponseForbidden("You are not allowed to edit this book.")

    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('book_detail', pk=book.pk)
    else:
        form = BookForm(instance=book)

    context = {'form': form, 'book': book}
    return render(request, 'books/edit_book.html', context)


@login_required
def delete_book(request, pk):
    book = get_object_or_404(Book, pk=pk)

    if book.posted_by != request.user:
        return HttpResponseForbidden("You are not allowed to delete this book.")

    if request.method == 'POST':
        book.delete()
        return redirect('homepage')

    context = {'book': book}
    return render(request, 'books/delete_book.html', context)

def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('homepage')
    else:
        form = RegisterForm()

    context = {'form': form}
    return render(request, 'books/register.html', context)


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('homepage')
    else:
        form = AuthenticationForm()

    context = {'form': form}
    return render(request, 'books/login.html', context)


def logout_view(request):
    logout(request)
    return redirect('homepage')