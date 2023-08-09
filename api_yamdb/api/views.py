from rest_framework import viewsets, mixins, filters
from rest_framework.exceptions import ValidationError
from rest_framework.permissions import SAFE_METHODS

from .serializers import TitlesSerializer, ReadTitleSerializer, GenreSerializer, CategorySerializer
from reviews.models import Titles, Genre, Category


class GenreViewSet(mixins.CreateModelMixin,
                   mixins.ListModelMixin,
                   viewsets.GenericViewSet,
                   mixins.DestroyModelMixin):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name',)


class CategoryViewSet(mixins.CreateModelMixin,
                      mixins.ListModelMixin,
                      viewsets.GenericViewSet,
                      mixins.DestroyModelMixin):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name',)


class TitlesViewSet(viewsets.ModelViewSet):
    queryset = Titles.objects.all()
    serializer_class = TitlesSerializer

    def perform_create(self, serializer):
        genre_names = self.request.data.get('genre', [])
        existing_genres = Genre.objects.filter(name__in=genre_names)
        if existing_genres.count() == len(genre_names):
            serializer.save()
        else:
            raise ValidationError("Указаны несуществующие жанры")

    def get_serializer_class(self):
        if self.action in SAFE_METHODS:
            return ReadTitleSerializer
        return TitlesSerializer
