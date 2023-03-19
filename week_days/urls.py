from django.urls import path
from . import views

urlpatterns = [
    path('<int:day>', views.days),
    path('<list_day>', views.weekday, name='week-name'),

]
