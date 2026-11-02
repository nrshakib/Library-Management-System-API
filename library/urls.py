from django.urls import path

from library import views


urlpatterns = [
    # author
    path('authors/', views.AuthorListCreateAPIView.as_view(), name='author-list-create'),
    path('author/<str:identifier>/', views.AuthorDetailAPIView.as_view(), name='author-details'),

    # category
    path('categories/', views.CategoryListCreateAPI.as_view(), name='category-list-create')
]