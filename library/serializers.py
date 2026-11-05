from datetime import datetime

from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from library.models import AuthorModel, BookModel, CategoryModel

class AuthorSummarySerializer(serializers.ModelSerializer):
    class Meta:
        model = AuthorModel
        fields = ['id', 'name', 'slug']

class CategorySummarySerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoryModel
        fields = ['id', 'name', 'slug']

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = AuthorModel
        fields = ['id', 'name', 'slug', 'biography', 'created_at'] # to display specific fields
        # fields = '__all__'  # to show all fields in response
        read_only_fields = ['id', 'slug', 'created_at']

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoryModel
        fields = '__all__'
        read_only_fields = ['id', 'slug', 'created_at']

class BookSerializer(serializers.ModelSerializer):
    author = AuthorSummarySerializer(read_only=True)
    category = CategorySummarySerializer(read_only=True)

    author_id = serializers.PrimaryKeyRelatedField(
        queryset=AuthorModel.objects.all(),
        source='author',
        write_only=True
    )
    category_id = serializers.PrimaryKeyRelatedField(
        queryset=CategoryModel.objects.all(),
        source='category',
        write_only=True
    )

    class Meta:
        model= BookModel
        fields = '__all__'
        read_only_fields = ['id', 'slug', 'created_at']

    def validate(self, attrs):
        published_year = attrs.get('published_year')
        current_year = datetime.now().year

        if published_year and published_year > current_year:
            raise ValidationError({
                "published_year": "Published year cannot be in the future."
            })

        return attrs

    def validate_available_copies(self, value):
        if value < 0:
            raise ValidationError("Available copies cannot be negative.")

        return value

    def validate_isbn(self, value):
        if len(value) < 10:
            raise ValidationError('ISBN must contain at least 10 characters.')
        
        return value