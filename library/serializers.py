from rest_framework import serializers

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

    class Meta:
        model= BookModel
        fields = '__all__'
        read_only_fields = ['id', 'slug', 'created_at']