from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('authors/', author_list, name='authors'),
    path('books/', book_list, name='book_list'),
]