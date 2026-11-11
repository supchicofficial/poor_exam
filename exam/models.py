from django.db import models

# Create your models here.

class Author(models.Model):
    name = models.CharField(max_length=100)
    book = models.ForeignKey('Book', related_name='authors',on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=100)
    caption = models.TextField()
    due_date = models.DateField()
    author = models.ForeignKey('Author', related_name='books', on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.title

class Order(models.Model):
    full_name = models.CharField(max_length=100)
    number_phone = models.CharField(max_length=20)
    book = models.ForeignKey('Book', related_name='orders', on_delete=models.CASCADE)
    buy = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.full_name