from rest_framework import serializers

from library.models import AuthorModel, BookModel, CategoryModel

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
    class Meta:
        model= BookModel
        fields = '__all__'
        read_only_fields = ['id', 'slug', 'created_at']