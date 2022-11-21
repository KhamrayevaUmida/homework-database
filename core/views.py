from django.shortcuts import render
from .models import *

def main(request):
    information = Main.objects.all()
    container = {
        'information': information
    }

    return render(request, 'index.html', container)


def car(request):
    information = Car.objects.all()
    container = {
        'information': information
    }

    return render(request, 'page/car.html', container)

def fruit(request):
    information = Fruit.objects.all()
    container = {
        'information': information
    }

    return render(request, 'page/fruit.html', container)

def animal(request):
    information = Animal.objects.all()
    container = {
        'information': information
    }

    return render(request, 'page/animal.html', container)

def telephone(request):
    information = Telephone.objects.all()
    container = {
        'information': information
    }

    return render(request, 'page/telephone.html', container)

def computer(request):
    information = Computer.objects.all()
    container = {
        'information': information
    }

    return render(request, 'page/computer.html', container)

def book(request):
    information = Book.objects.all()
    container = {
        'information': information
    }

    return render(request, 'page/book.html', container)

def texnika(request):
    information = Texnika.objects.all()
    container = {
        'information': information
    }

    return render(request, 'page/texnika.html', container)

def color(request):
    information = Color.objects.all()
    container = {
        'information': information
    }

    return render(request, 'page/color.html', container)


def mebel(request):
    information = Mebel.objects.all()
    container = {
        'information': information
    }

    return render(request, 'page/mebel.html', container)