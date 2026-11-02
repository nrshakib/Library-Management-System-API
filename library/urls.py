from django.urls import path

from library import views


urlpatterns = [
    path('authors/', views.AuthorListCreateAPIView.as_view(), name='author-list-create'),
    path('author/<str:identifier>/', views.AuthorDetailAPIView.as_view(), name='author-details'),
]