from django.shortcuts import render

from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from books import models
from books import serializers


class GenreViewSet(ModelViewSet):
    """ ViewSet for Genre model """
    queryset = models.Genre.objects.all()
    serializer_class = serializers.GenreSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, ]
    

class BookViewSet(ModelViewSet):
    """ ViewSet for Book model """
    queryset = models.Book.objects.all()
    serializer_class = serializers.BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, ]


class CommentViewSet(ModelViewSet):
    """ ViewSet for Book comment """
    queryset = models.Comment.objects.all()
    serializer_class = serializers.CommentSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, ]
    