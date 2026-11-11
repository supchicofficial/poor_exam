from .views import *
import os
from django.urls import path

urlpatterns = [
    path('books/', book_list, name='book_list'),
    path('authors/', author_list, name='author_list'),
    path('orders/', order_list, name='order_list'),
]