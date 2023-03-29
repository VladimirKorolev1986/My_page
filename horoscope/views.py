from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string

zodiac_dict = {

    'aries': 'Овен - первый знак зодиака, планета Марс (с 21 марта по 20 апреля).',
    'taurus': 'Телец - второй знак зодиака, планета Венера (с 21 апреля по 21 мая).',
    'gemini': 'Близнецы - третий знак зодиака, планета Меркурий (с 22 мая по 21 июня).',
    'cancer': 'Рак - четвёртый знак зодиака, Луна (с 22 июня по 22 июля).',
    'leo': 'Лев - пятый знак зодиака, солнце (с 23 июля по 21 августа).',
    'virgo': 'Дева - шестой знак зодиака, планета Меркурий (с 22 августа по 23 сентября).',
    'libra': 'Весы - седьмой знак зодиака, планета Венера (с 24 сентября по 23 октября).',
    'scorpio': 'Скорпион - восьмой знак зодиака, планета Марс (с 24 октября по 22 ноября).',
    'sagittarius': 'Стрелец - девятый знак зодиака, планета Юпитер (с 23 ноября по 22 декабря).',
    'capricorn': 'Козерог - десятый знак зодиака, планета Сатурн (с 23 декабря по 20 января).',
    'aquarius': 'Водолей - одиннадцатый знак зодиака, планеты Уран и Сатурн (с 21 января по 19 февраля).',
    'pisces': 'Рыбы - двенадцатый знак зодиака, планеты Юпитер (с 20 февраля по 20 марта).',

}
zodiac_types = {'fire': ['aries', 'taurus', 'gemini'],
                'earth': ['cancer', 'leo', 'virgo'],
                'air': ['libra', 'scorpio', 'sagittarius'],
                'water': ['capricorn', 'aquarius', 'pisces']}


def get_info_about_sign_zodiac(request, sing_zodiac):
    description = zodiac_dict.get(sing_zodiac)
    data = {
        'description_zodiac': description,
        'sing': sing_zodiac
    }
    return render(request, 'horoscope/info_zodiac.html', context=data)


def get_info_about_sign_zodiac_by_number(request, sing_zodiac: int):
    if sing_zodiac > len(zodiac_dict):
        return HttpResponseNotFound(f'Неправильный порядковый номер знака зодиака - {sing_zodiac}')
    name_zodiac = list(zodiac_dict)[sing_zodiac - 1]
    redirect_url = reverse('horoscope-name', args=(name_zodiac,))
    return HttpResponseRedirect(redirect_url)


def index(request):
    name_zodiacs = list(zodiac_dict)
    # f'<li><a href="{redirect_path}">{sing.title()}</a></li>'
    context = {
        'name_zodiacs': name_zodiacs,
        'zodiac_dict': zodiac_dict
    }

    return render(request, 'horoscope/index.html', context=context)


def types_sign_zodiac(request):
    name_type = list(zodiac_types)
    res = ''
    count = 0
    for type in name_type:
        redirect_path = reverse('horoscope-types', args=(type,))
        res += f'<li><a href="{redirect_path}">{type.title()}</a></li>'

    response = f"""
        <ol>
            {res}
        </ol>
        """
    return HttpResponse(response)


def sings_type_zodiac(request, sint_type_zodiac):
    list_zodiac_type = zodiac_types[sint_type_zodiac]
    if list_zodiac_type:
        res = ''
        for sing in list_zodiac_type:
            redirect_path = reverse('horoscope-name', args=(sing,))
            res += f'<li><a href="{redirect_path}">{sing}</a></li>'
        response = f"""
        <ol>
            {res}
        </ol>    
        """
        return HttpResponse(response)


dct_day = {
    (110, 140): 'aries',
    (141, 171): 'taurus',
    (172, 202): 'gemini',
    (203, 233): 'cancer',
    (234, 264): 'leo',
    (265, 295): 'virgo',
    (296, 326): 'libra',
    (327, 357): 'scorpio',
    (356, 386): 'sagittarius',

}


def get_info_by_date(request, month, day):
    sing = ''
    day_in_year = month * 30 + day
    for date in dct_day:
        if date[0] <= day_in_year <= date[1]:
            sing = dct_day[date]

    return HttpResponse(f'месяц - {month}, день - {day}, и знак зодиака {sing}')


"""21 марта – 20 апреля Овен
21 апреля – 21 мая Телец
22 мая – 21 июня Близнецы
22 июня – 22 июля Рак
23 июля – 23 августа Лев
24 августа – 22 сентября Дева
23 сентября – 22 октября Весы
23 октября – 22 ноября Скорпион
22 ноября – 21 декабря Стрелец
22 декабря – 20 января Козерог
21 января – 19 февраля Водолей
20 февраля – 20 марта Рыбы."""
