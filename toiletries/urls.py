from django.urls import path
from . import views

app_name = 'toiletries'

urlpatterns = [
    path('', views.toiletries_view, name='toiletries'),
] 