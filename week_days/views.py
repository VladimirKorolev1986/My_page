from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
dct = {
    'monday': 'в понедельник я жалею себя',
    'tuesday': 'во вторник - глазею в пропасть',
    'wednesday': 'в среду решаю проблему мирового голода (никому не говорите)',
    'thursday ': 'в четверг - зарядка',
    'friday ': 'ужин с собой, нельзя снова его пропускать',
    'saturday ': 'в субботу - борьба с презрением к себе',
    'sunday ': 'в воскресенье - иду на рождество'
}


# def weekday(request, list_day):
#     if list_day not in dct:
#         return HttpResponseNotFound("Нет такой страницы")
#     return HttpResponse(f'{dct[list_day]}')

def weekday(request, list_day):
    if list_day not in dct:
        return HttpResponseNotFound("Нет такой страницы")
    return render(request, 'week_days/greeting.html')


def days(response, day: int):

    if day > len(dct):
        return HttpResponseNotFound('Нет такого дня')
    name_day = list(dct)[day - 1]
    redirect_week = reverse('week-name', args=(name_day, ))
    return HttpResponseRedirect(redirect_week)
