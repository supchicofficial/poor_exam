from django.shortcuts import render, redirect
from .models import Author, Book


def index(request):
    return render(request, 'index.html')

def author_list(request):
    if request.method == 'POST':
        action = request.POST.get('action')
        if action == 'create':
            name = request.POST.get('name')
            Author.objects.create(name=name)
        elif action == 'update':
            author_id = request.POST.get('author_id')
            author = Author.objects.get(id=author_id)
            author.name = request.POST.get('name')
            author.save()
        elif action == 'delete':
            author_id = request.POST.get('author_id')
            author = Author.objects.get(id=author_id)
            author.delete()
        return redirect('author_list')
    authors = Author.objects.all()
    return render(request, 'author.html', {
        'authors': authors
    })


def book_list(request):
    books = Book.objects.all()
    return render(request, 'book.html', {
        'books': books
    })