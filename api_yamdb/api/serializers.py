from rest_framework import serializers

from reviews.models import Titles, Category, Genre


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ('name', 'slug')


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('name', 'slug')


class TitlesSerializer(serializers.ModelSerializer):

    genre = serializers.SlugRelatedField(
        slug_field='name',
        queryset=Genre.objects.all(),
        many=True
    )

    category = serializers.SlugRelatedField(
        slug_field='name',
        queryset=Category.objects.all(),)

    class Meta:
        model = Titles
        fields = '__all__'


class ReadTitleSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    genre = GenreSerializer(read_only=True, many=True)

    class Meta:
        model = Titles
        fields = "__all__"
