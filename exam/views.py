from django.shortcuts import render, redirect
from django.http import HttpResponse

def index(request):
    return render(request, 'index.html')


def book_list(request):
    title = "Список книг"
    context = {
        'title': title
    }
    post = request.POST.get('post')
    if post:
        return redirect('book_list')
    return render(request, 'book_list.html', context)


def author_list(request):
    title = "Список авторов"
    context = {
        'title': title
    }
    post = request.POST.get('post')
    if post:
        return redirect('author_list')
    return render(request, 'author_list.html', context)


def order_list(request):
    title = "Список заказов"
    context = {
        'title': title
    }
    post = request.POST.get('post')
    if post:
        return redirect('order_list')
    return render(request, 'order_list.html', context)