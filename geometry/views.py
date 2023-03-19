import math

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from math import pi
from django.urls import reverse


def get_rectangle_area(request, width, height):
    s = width * height
    return HttpResponse(f'Площадь прямоугольник размером {width} на {height} равна {s}')


def get_square_area(request, width):
    s = width ** 2
    return HttpResponse(f'Площадь квадрата размером {width} на {width} равна {s}')


def get_circle_area(request, radius):
    s = math.pi * radius ** 2
    return HttpResponse(f'Площадь круга диаметром {radius} равна {s.__round__(3)}')


def redirect_rect(request, width, height):
    redirect_rectangle = reverse('rectangle-area', args=(width, height,))
    return HttpResponseRedirect(redirect_rectangle)


def redirect_square(request, width):
    redirect_sq = reverse('square-area', args=(width,))
    return HttpResponseRedirect(redirect_sq)


def redirect_circle(request, radius):
    redirect_cir = reverse('circle-area', args=(radius,))
    return HttpResponseRedirect(redirect_cir)
