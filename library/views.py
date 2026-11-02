from django.db.models import Q
from django.shortcuts import get_object_or_404, render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from library.models import AuthorModel, BookModel, CategoryModel
from library.serializers import AuthorSerializer, BookSerializer, CategorySerializer

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

    def put(self, request, identifier):
        incoming_data = request.data
        if identifier.isdigit():
            author = get_object_or_404(AuthorModel, id=int(identifier))
        else:
            author = get_object_or_404(AuthorModel, slug=identifier)

        serializer = AuthorSerializer(author,data=incoming_data)

        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response({
            "message": "Author updated successfully",
            "data": serializer.data
        })

    def patch(self, request, identifier):
        incoming_data = request.data

        if identifier.isdigit():
            author = get_object_or_404(AuthorModel, id=int(identifier))
        else:
            author = get_object_or_404(AuthorModel, slug=identifier)

        serializer = AuthorSerializer(author, data=incoming_data, partial=True)
        
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response({
            "message": "Author updated successfully",
            "data": serializer.data
        })

    def delete(self, request, identifier):
        if identifier.isdigit():
            author = get_object_or_404(AuthorModel, id=int(identifier))
        else:
            author = get_object_or_404(AuthorModel, slug=identifier)

        author.delete()

        return Response({
            "message": "Author deleted successfully"
        }, status=status.HTTP_200_OK)

class CategoryListCreateAPI(APIView):
    def get(self, request):
        category_data = CategoryModel.objects.all()
        serializer = CategorySerializer(category_data, many=True)

        return Response({
            "message": "Categories retrieved successfully",
            "data": serializer.data
        },
            status= status.HTTP_200_OK
        )

    def post(self, request):
        incoming_data= request.data
        serializer = CategorySerializer(data=incoming_data)

        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response({
            "message": "Category created successfully",
            "data": serializer.data
        },
            status= status.HTTP_201_CREATED
        )

class CategoryDetailsAPI(APIView):
    def get_category(self, identifier):
        if identifier.isdigit():
            category = get_object_or_404(CategoryModel, id=int(identifier))
        else:
            category = get_object_or_404(CategoryModel, slug=identifier)

        return category

    def get(self, request, identifier):
        category = self.get_category(identifier)
        serializer = CategorySerializer(category)

        return Response({
            "message": "Category retrieved successfully",
            "data": serializer.data
        },
            status= status.HTTP_200_OK
        )


    def put(self, request, identifier):
        incoming_data = request.data
        category = self.get_category(identifier)
        serializer = CategorySerializer(category, data=incoming_data)

        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response({
            "message": "Category updated successfully",
            "data": serializer.data
        },
            status= status.HTTP_200_OK
        )

    def patch(self, request, identifier):
        incoming_data = request.data
        category = self.get_category(identifier)
        serializer = CategorySerializer(category, data=incoming_data, partial=True)

        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response({
            "message": "Category updated successfully",
            "data": serializer.data
        },
            status= status.HTTP_200_OK
        )

    def delete(self, request, identifier):
        category = self.get_category(identifier)

        category.delete()
        
        return Response({
            "message": "Category deleted successfully",
            "data": None
        },
            status= status.HTTP_200_OK
        )

class BookListCreateAPIView(APIView):
    def get(self, request):
        books = BookModel.objects.all()
        serializer = BookSerializer(books, many=True)

        return Response({
            "message": "All books retrieved successfully",
            "data": serializer.data
        }, status=status.HTTP_200_OK )

    def post(self, request):
        incoming_data = request.data
        serializer = BookSerializer(data=incoming_data)

        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response({
            "message": "Book created successfully",
            "data": serializer.data
            }, status=status.HTTP_201_CREATED
        )

class BookDetailAPIView(APIView):
    def get_book(self, identifier):
        if identifier.isdigit():
            book = get_object_or_404(BookModel, id=int(identifier))
        else:
            book = get_object_or_404(BookModel, slug=identifier)

        return book

    def get(self, request, identifier):
        book = self.get_book(identifier)
        serializer = BookSerializer(book)

        return Response({
            "message": "Book retrieved successfully",
            "data": serializer.data
        }, status= status.HTTP_200_OK )

    def put(self, request, identifier):
        incoming_data = request.data
        book = self.get_book(identifier)
        serializer = BookSerializer(book, data=incoming_data)

        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response({
            "message": "Book updated successfully",
            "data": serializer.data
        },status=status.HTTP_200_OK )

    def patch(self, request, identifier):
            incoming_data = request.data
            book = self.get_book(identifier)
            serializer = BookSerializer(book, data=incoming_data, partial=True)
    
            serializer.is_valid(raise_exception=True)
            serializer.save()
    
            return Response({
                "message": "Book updated successfully",
                "data": serializer.data
            },status=status.HTTP_200_OK )

    def delete(self, request, identifier):
            book = self.get_book(identifier)
    
            book.delete()
    
            return Response({
                "message": "Book deleted successfully",
                "data": None
            },status=status.HTTP_200_OK )