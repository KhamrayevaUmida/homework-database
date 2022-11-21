from django.db import models

class Main(models.Model):
    name = models.CharField(max_length=256)
    image = models.CharField(max_length=256)
    content = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Car(models.Model):
    name = models.CharField(max_length=256)
    image = models.CharField(max_length=256)
    comment = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Fruit(models.Model):
    name = models.CharField(max_length=256)
    image = models.CharField(max_length=256)
    color = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Animal(models.Model):
    name = models.CharField(max_length=256)
    image = models.CharField(max_length=256)
    comment = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Telephone(models.Model):
    name = models.CharField(max_length=256)
    image = models.CharField(max_length=256)
    version = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Computer(models.Model):
    name = models.CharField(max_length=256)
    image = models.CharField(max_length=256)
    processor = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Book(models.Model):
    name = models.CharField(max_length=256)
    image = models.CharField(max_length=256)
    biografiya = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Texnika(models.Model):
    name = models.CharField(max_length=256)
    image = models.CharField(max_length=256)
    comment = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Color(models.Model):
    name = models.CharField(max_length=256)
    image = models.CharField(max_length=256)
    exemple = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Mebel(models.Model):
    name = models.CharField(max_length=256)
    image = models.CharField(max_length=256)
    tasvir = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name