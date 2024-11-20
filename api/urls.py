from django.urls import path, include
from . import views

app_name = "api"
urlpatterns = [
    path('user_marks/', views.user_marks, name='get_user_markers'),
    path('add_marker/', views.add_marker, name='add_marker'),
    path('remove_marker/', views.remove_marker, name='remove_marker'),
    path('check_marker/', views.check_marker, name='check_marker'),
    path('api_test/', views.api_test, name='api_test'),
]
