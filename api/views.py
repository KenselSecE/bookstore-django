from rest_framework.decorators import api_view
from rest_framework.response import Response
from books.models import Book
from .serializers import BookSerializer

@api_view(['GET'])
def get_routes(request):
    routes = [
        {'method': 'GET', 'path': '/api/'},
        {'method': 'GET', 'path': '/api/books/'},
        {'method': 'GET', 'path': '/api/books/<id>/'},
    ]
    return Response(routes)

@api_view(['GET'])
def get_books(request):
    books = Book.objects.all()
    serializer = BookSerializer(books, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def get_book(request, pk):
    book = Book.objects.get(pk=pk)
    serializer = BookSerializer(book)
    return Response(serializer.data)