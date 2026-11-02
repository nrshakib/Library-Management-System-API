from django.shortcuts import render
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