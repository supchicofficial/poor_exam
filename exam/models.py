from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author,on_delete=models.CASCADE,related_name='books')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    def __str__(self):
        return self.title



class Order(models.Model):
    full_name = models.CharField(max_length=100)
    number_phone = models.CharField(max_length=20)
    book = models.ForeignKey(Book,related_name='orders',on_delete=models.CASCADE)
    buy = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.full_name