from django.shortcuts import render
from django.http import HttpResponse

def first(request):
    return HttpResponse('<h1> i would like to dance </h1>')


def second(request):
    return HttpResponse('<h1> i would like to draw </h1>')


