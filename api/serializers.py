from rest_framework import serializers

from .models import Book, LibUser, RentBook


class BookSerializer(serializers.ModelSerializer):

    class Meta:
        model = Book
        fields = '__all__'


class LibUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = LibUser
        fields = '__all__'


class RentBookSerializer(serializers.ModelSerializer):

    class Meta:
        model = RentBook
        fields = '__all__'
