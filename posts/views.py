from django.shortcuts import render
from django.http import HttpResponse


def post(request, number_post):
    return HttpResponse(f'Здесь содержится информация о посте под номером {number_post}')


def post_string(request, name_post):
    return HttpResponse(f'Информация о посте {name_post}')
