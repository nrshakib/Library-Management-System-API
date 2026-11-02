from django.urls import path

from library import views


urlpatterns = [
    path('authors/', views.AuthorListCreateAPIView.as_view(), name='author-list-create')
]