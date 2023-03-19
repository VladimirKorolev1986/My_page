from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('<int:sing_zodiac>', views.get_info_about_sign_zodiac_by_number),
    path('<str:sing_zodiac>', views.get_info_about_sign_zodiac, name='horoscope-name'),
    # path('type/<str:types_zodiac>', views.types_sign_zodiac, name='horoscope-types'),
    path('type/', views.types_sign_zodiac, name='horoscope-types'),
    path('type/<sint_type_zodiac>', views.sings_type_zodiac),

]
