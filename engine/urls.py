from django.urls import path
from . import views

urlpatterns = [
    path('', views.search, name='search'),
    path('video', views.video, name='video'),
    path('delete', views.delete, name='delete'),
]