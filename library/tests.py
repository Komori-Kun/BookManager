from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Author, Book

class AuthorTests(APITestCase):
    def setUp(self):
        self.author_name = 'Luciano Ramalho'
        self.author = Author.objects.create(name=self.author_name)

    def test_create_author(self):
        url = reverse('author-list')
        data = {'name': 'New Author'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Author.objects.count(), 2)
        self.assertEqual(Author.objects.get(id=2).name, 'New Author')

    def test_get_authors(self):
        url = reverse('author-list')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['name'], self.author_name)

class BookTests(APITestCase):
    def setUp(self):
        self.author = Author.objects.create(name='Luciano Ramalho')
        self.book = Book.objects.create(name='Python Book', edition=1, publication_year=2021)
        self.book.authors.add(self.author)

    def test_create_book(self):
        url = reverse('book-list')
        data = {
            'name': 'New Book',
            'edition': 2,
            'publication_year': 2023,
            'authors': [self.author.id]
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 2)
        self.assertEqual(Book.objects.get(id=2).name, 'New Book')

    def test_get_books(self):
        url = reverse('book-list')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['name'], 'Python Book')

# Create your tests here.
