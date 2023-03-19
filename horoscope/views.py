from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

zodiac_dict = {'Fire': {'aries': 'Овен - первый знак зодиака, планета Марс (с 21 марта по 20 апреля).',
                        'taurus': 'Телец - второй знак зодиака, планета Венера (с 21 апреля по 21 мая).',
                        'gemini': 'Близнецы - третий знак зодиака, планета Меркурий (с 22 мая по 21 июня).'},
               'Earth': {'cancer': 'Рак - четвёртый знак зодиака, Луна (с 22 июня по 22 июля).',
                         'leo': 'Лев - пятый знак зодиака, солнце (с 23 июля по 21 августа).',
                         'virgo': 'Дева - шестой знак зодиака, планета Меркурий (с 22 августа по 23 сентября).'},
               'Air': {'libra': 'Весы - седьмой знак зодиака, планета Венера (с 24 сентября по 23 октября).',
                       'scorpio': 'Скорпион - восьмой знак зодиака, планета Марс (с 24 октября по 22 ноября).',
                       'sagittarius': 'Стрелец - девятый знак зодиака, планета Юпитер (с 23 ноября по 22 декабря).'},
               'Water': {'capricorn': 'Козерог - десятый знак зодиака, планета Сатурн (с 23 декабря по 20 января).',
                         'aquarius': 'Водолей - одиннадцатый знак зодиака,'
                                     ' планеты Уран и Сатурн (с 21 января по 19 февраля).',
                         'pisces': 'Рыбы - двенадцатый знак зодиака, планеты Юпитер (с 20 февраля по 20 марта).'}

               }


def get_info_about_sign_zodiac(request, sing_zodiac):
    description = zodiac_dict.get(sing_zodiac)
    if description:
        return HttpResponse(f'<h2>{description}</h2>')
    else:
        HttpResponseNotFound(f'Нет такого знака зодиака - {sing_zodiac}')
    # if sing_zodiac not in zodiac_dict:
    #     return HttpResponseNotFound('Нет такого знака зодиака')
    # return HttpResponse(f'{zodiac_dict[sing_zodiac]}')


def get_info_about_sign_zodiac_by_number(request, sing_zodiac: int):
    if sing_zodiac > len(zodiac_dict):
        return HttpResponseNotFound(f'Неправильный порядковый номер знака зодиака - {sing_zodiac}')
    name_zodiac = list(zodiac_dict)[sing_zodiac - 1]
    redirect_url = reverse('horoscope-name', args=(name_zodiac,))
    return HttpResponseRedirect(redirect_url)


def index(request):
    name_zodiac = list(zodiac_dict)

    res = ''
    for sing in name_zodiac:
        redirect_path = reverse('horoscope-name', args=(sing,))
        res += f'<li><a href="{redirect_path}">{sing.title()}</a></li>'
    response = f"""
    <ol>
        {res}    
    </ol>
    """
    return HttpResponse(response)


def types_sign_zodiac(request):
    for type in zodiac_dict:
        print(type)
