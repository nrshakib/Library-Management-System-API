from django.core.serializers import serialize
from django.db.models import Q
from django.shortcuts import get_object_or_404, render
from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from library.models import AuthorModel, BookModel, CategoryModel
from library.serializers import AuthorSerializer, BookSerializer, CategorySerializer
from utils.utils import api_response

class AuthorListCreateGenericAPIView(GenericAPIView):
    queryset = AuthorModel.objects.all()
    serializer_class = AuthorSerializer

    def get(self, request):
        authors = self.get_queryset()
        serializer = self.get_serializer(authors, many=True)

        return api_response(
            message= "Authors retrieved successfully",
            data= serializer.data,
            status_code=status.HTTP_200_OK
        )

    def post(self, request):
        incoming_data = request.data
        serializer = self.get_serializer(data=incoming_data)

        serializer.is_valid(raise_exception=True)
        serializer.save()

        return api_response(
            message= "Author created successfully",
            data= serializer.data,
            status_code=status.HTTP_201_CREATED
        )
    
class AuthorDetailGenericAPIView(GenericAPIView):
    queryset = AuthorModel.objects.all()
    serializer_class = AuthorSerializer

    def identifier_is_id(self, identifier):
            # returns true if identifier is totally numeric/digit
            # returns false if identifier contains characters alongside or without digits
            return identifier.isdigit()
    
    def get_object(self):
        # get the identifier from the url parameter: kwargs = url parameter
        identifier = self.kwargs.get('identifier')
    
        # If the identifier contains only digits, convert it to an integer and fetch the author by id.
        if self.identifier_is_id(identifier):
            return get_object_or_404(
                self.get_queryset(), id=int(identifier))
    
        # if identifier contains any character, fetch author based on slug
        else:
            return get_object_or_404(
                self.get_queryset(), slug=identifier)
            
    # here detail can be fetched using id or slug
    def get(self, request, identifier):
        author = self.get_object()
        serializer = self.get_serializer(author)

        return api_response(
            message= "Author retrieved successfully",
            data= serializer.data,
            status_code=status.HTTP_200_OK
        )
        
    def put(self, request, identifier):
        incoming_data = request.data
        author = self.get_object()
        serializer = self.get_serializer(author, data=incoming_data)

        serializer.is_valid(raise_exception=True)
        serializer.save()

        return api_response(
            message= "Author updated successfully",
            data= serializer.data,
            status_code=status.HTTP_200_OK
        )

    def patch(self, request, identifier):
        incoming_data = request.data
        author = self.get_object()
        serializer = self.get_serializer(author, data=incoming_data, partial=True)
        
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return api_response(
            message= "Author updated successfully",
            data= serializer.data,
            status_code=status.HTTP_200_OK
        )

    def delete(self, request, identifier):
        author = self.get_object()
        author.delete()

        return api_response(
            message= "Author deleted successfully",
            data= None,
            status_code=status.HTTP_200_OK
        )

class CategoryListCreateGenericAPIView(GenericAPIView):
    queryset = CategoryModel.objects.all()
    serializer_class = CategorySerializer

    def get(self, request):
        categories = self.get_queryset()
        serializer = self.get_serializer(categories, many=True)

        return api_response(
            message= "Categories retrieved successfully",
            data= serializer.data,
            status_code=status.HTTP_200_OK
        )

    def post(self, request):
        incoming_data= request.data
        serializer = self.get_serializer(data=incoming_data)

        serializer.is_valid(raise_exception=True)
        serializer.save()

        return api_response(
            message= "Category created successfully",
            data= serializer.data,
            status_code=status.HTTP_201_CREATED
        )

class CategoryDetailGenericAPIView(GenericAPIView):
    queryset = CategoryModel.objects.all()
    serializer_class = CategorySerializer

    def identifier_is_id(self, identifier):
        return identifier.isdigit()

    def get_object(self):
        identifier = self.kwargs.get('identifier')
    
        if self.identifier_is_id(identifier):
            return get_object_or_404(
                self.get_queryset(), id=int(identifier))
    
        else:
            return get_object_or_404(
                self.get_queryset(), slug=identifier)

    def get(self, request, identifier):
        category = self.get_object()
        serializer = self.get_serializer(category)

        return api_response(
            message= "Category retrieved successfully",
            data= serializer.data,
            status_code=status.HTTP_200_OK
        )


    def put(self, request, identifier):
        incoming_data = request.data
        category = self.get_object()
        serializer = self.get_serializer(category, data=incoming_data)

        serializer.is_valid(raise_exception=True)
        serializer.save()

        return api_response(
            message= "Category updated successfully",
            data= serializer.data,
            status_code=status.HTTP_200_OK
        )

    def patch(self, request, identifier):
        incoming_data = request.data
        category = self.get_object()
        serializer = self.get_serializer(category, data=incoming_data, partial=True)

        serializer.is_valid(raise_exception=True)
        serializer.save()

        return api_response(
            message= "Category updated successfully",
            data= serializer.data,
            status_code=status.HTTP_200_OK
        )

    def delete(self, request, identifier):
        category = self.get_object()
        category.delete()
        
        return api_response(
            message= "Category deleted successfully",
            data= None,
            status_code=status.HTTP_200_OK
        )

class BookListCreateGenericAPIView(GenericAPIView):
    queryset = BookModel.objects.all()
    serializer_class = BookSerializer

    def get(self, request):
        books = self.get_queryset()
        serializer = self.get_serializer(books, many=True)

        return api_response(
            message= "Books retrieved successfully",
            data= serializer.data,
            status_code=status.HTTP_200_OK
        )

    def post(self, request):
        incoming_data = request.data
        serializer = self.get_serializer(data=incoming_data)

        serializer.is_valid(raise_exception=True)
        serializer.save()

        return api_response(
            message= "Book created successfully",
            data= serializer.data,
            status_code=status.HTTP_201_CREATED
        )

class BookDetailGenericAPIView(GenericAPIView):
    queryset = BookModel.objects.all()
    serializer_class=BookSerializer
    def identifier_is_id(self, identifier):
        return identifier.isdigit()

    def get_object(self):
        identifier = self.kwargs.get('identifier')

        if self.identifier_is_id(identifier):
            return get_object_or_404(self.get_queryset(), id=int(identifier))
        else:
            return get_object_or_404(self.get_queryset(), slug=identifier)

    def get(self, request, identifier):
        book = self.get_object()
        serializer = self.get_serializer(book)

        return api_response(
            message= "Book retrieved successfully",
            data= serializer.data,
            status_code= status.HTTP_200_OK )

    def put(self, request, identifier):
        incoming_data = request.data
        book = self.get_object()
        serializer = self.get_serializer(book, data=incoming_data)

        serializer.is_valid(raise_exception=True)
        serializer.save()

        return api_response(
            message= "Book updated successfully",
            data= serializer.data,
            status_code=status.HTTP_200_OK )

    def patch(self, request, identifier):
            incoming_data = request.data
            book = self.get_object()
            serializer = self.get_serializer(book, data=incoming_data, partial=True)
    
            serializer.is_valid(raise_exception=True)
            serializer.save()
    
            return api_response(
                message= "Book updated successfully",
                data= serializer.data,
                status_code=status.HTTP_200_OK )

    def delete(self, request, identifier):
            book = self.get_object()
            book.delete()
    
            return api_response(
                message= "Book deleted successfully",
                data= None,
                status_code=status.HTTP_200_OK )