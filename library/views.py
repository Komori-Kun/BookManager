from rest_framework import viewsets
from .models import Author, Book
from .serializers import AuthorSerializer, BookSerializer

class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        name = self.request.query_params.get('name', None)
        year = self.request.query_params.get('publication_year', None)
        edition = self.request.query_params.get('edition', None)
        author = self.request.query_params.get('author', None)
        
        if name:
            queryset = queryset.filter(name__icontains=name)
        if year:
            queryset = queryset.filter(publication_year=year)
        if edition:
            queryset = queryset.filter(edition__icontains=edition)
        if author:
            queryset = queryset.filter(authors__name__icontains=author)
        
        return queryset
    
