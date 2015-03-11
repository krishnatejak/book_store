from django.db import models


class Book(models.Model):
    name = models.CharField(max_length=2048)
    description = models.TextField(null=True)
    isbn = models.CharField(max_length=13)
    publisher = models.CharField(max_length=1024)
    cover_picture = models.FilePathField()
    price = models.DecimalField()
    stock = models.IntegerField(default=0)
    type = models.IntegerField(default=1)


class User(models.Model):
    username = models.CharField(max_length=128)
    password = models.CharField(max_length=128)
    first_name = models.CharField(max_length=128)
    middle_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128)



class Address(models.Model):
    user = models.ForeignKey(User)
    address = models.TextField()
    street_name = models.CharField(max_length=256, null=True)
    city = models.CharField(max_length=128)


class Phone(models.Model):
    user = models.ForeignKey
    number = models.CharField(max_length=20)


class CreditCard(models.Model):
    number = models.CharField(max_length=19)
    expiry = models.CharField(max_length=5)
    cvv = models.CharField(max_length=3)
    name = models.CharField(max_length=128)
    type = models.IntegerField(default=1)
    user = models.ForeignKey(User)


class Rating(models.Model):
    book = models.ForeignKey(Book)
    user = models.ForeignKey(User)
    start = models.IntegerField(default=0)


class Comment(models.Model):
    rating = models.ForeignKey(Rating)
    text = models.TextField()


class Order(models.Model):
    user = models.ForeignKey(User)
    date = models.DateTimeField(auto_now=True)
    quantity = models.IntegerField(default=0)
    price = models.DecimalField(default=0)
    discount = models.DecimalField(default=0)
    tax = models.DecimalField(default=0)

class BookOrder(models.Model):
    order = models.ForeignKey(Order)
    book = models.ForeignKey(User)






