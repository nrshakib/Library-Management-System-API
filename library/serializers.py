from rest_framework import serializers

from library.models import AuthorModel


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = AuthorModel
        fields = ['id', 'name', 'slug', 'biography', 'created_at'] # to display specific fields
        # fields = '__all__'  # to show all fields in response
        read_only_fields = ['id', 'slug', 'created_at']