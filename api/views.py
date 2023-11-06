from django.shortcuts import render
from rest_framework import viewsets

from api.models import Book, RentBook, LibUser
from api.serializers import BookSerializer, RentBookSerializer, LibUserSerializer



   
def cat():
    return f'Miy-Miy'


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class RentBookViewSet(viewsets.ModelViewSet):
    queryset = RentBook.objects.all()
    serializer_class = RentBookSerializer


class LibUserViewSet(viewsets.ModelViewSet):
    queryset = LibUser.objects.all()
    serializer_class = LibUserSerializer

   
   
   