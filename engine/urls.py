from django.urls import path
from django.views.generic import RedirectView
from . import views

app_name = "engine"

urlpatterns = [
    path('film/<str:film_name>', views.search, name='search'),
    path('', views.index, name='index'),
    path('video', views.video, name='video'),
    path('delete', views.delete, name='delete'),
]