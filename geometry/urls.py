from django.urls import path
from . import views

urlpatterns = [
    path('rectangle/<int:width>/<int:height>', views.get_rectangle_area, name='rectangle-area'),
    path('square/<int:width>', views.get_square_area, name='square-area'),
    path('geometry/<int:radius>', views.get_circle_area, name='geometry-area'),

    path('get_rectangle_area/<int:width>/<int:height>', views.redirect_rect),
    path('get_square_area/<int:width>', views.redirect_square),
    path('get_circle_area/<int:radius>', views.redirect_circle),

    path('<figure>/', views.figure),

    # path('square/', views.get_square_area, name='square-area'),
    # path('geometry/', views.get_circle_area, name='geometry-area')

]
