from django.urls import path
from . import views

urlpatterns = [
    path('<int:number_post>', views.post),
    path('<name_post>', views.post_string),
]
