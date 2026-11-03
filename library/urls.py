from django.urls import path

from library import views


urlpatterns = [
    # author
    path('authors/', views.AuthorListCreateGenericAPIView.as_view(), name='author-list-create'),
    path('author/<str:identifier>/', views.AuthorDetailGenericAPIView.as_view(), name='author-details'),

    # category
    path('categories/', views.CategoryListCreateGenericAPIView.as_view(), name='category-list-create'),
    path('category/<str:identifier>/', views.CategoryDetailGenericAPIView.as_view(), name='category-details'),

    # books
    path('books/', views.BookListCreateAPIView.as_view(), name='book-list-create'),
    path('book/<str:identifier>/', views.BookDetailAPIView.as_view(), name='book-detail')
]