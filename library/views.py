from django.db.models import Q
from django.shortcuts import get_object_or_404, render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from library.models import AuthorModel
from library.serializers import AuthorSerializer

class AuthorListCreateAPIView(APIView):
    def get(self, request):
        author_data = AuthorModel.objects.all()
        serializer = AuthorSerializer(author_data, many=True)

        return Response({
            "message": "Author retrieved successfully",
            "data": serializer.data
            },
            status= status.HTTP_200_OK
        )


    def post(self, request):
        data = request.data
        serializer = AuthorSerializer(data = data)

        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response({
             "message": "Author created successfully",
             "data": serializer.data
            },status= status.HTTP_201_CREATED
    )

class AuthorDetailAPIView(APIView):
    # here detail can be fetched using id or slug
    def get(self, request, identifier):

        # method 1 to fetch detail using id and slug
        # used Q to apply multiple query condition to fetch identifier
        # author = get_object_or_404(AuthorModel, Q(id=identifier) | Q(slug=identifier))

        # method 2 to fetch detail using id and slug
        # isdigit() is a string method to check if the string item contains only digit or not
        if identifier.isdigit():
            # If the identifier contains only digits, convert it to an integer and fetch the author by ID.
            author = get_object_or_404(AuthorModel, id=int(identifier))
        else:
            author = get_object_or_404(AuthorModel, slug=identifier)

        serializer = AuthorSerializer(author)

        return Response({
            "message": "Author retrieved successfully",
            "data": serializer.data
        })



