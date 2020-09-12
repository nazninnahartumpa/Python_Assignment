from django.urls import path
from calApp import views


urlpatterns = [
    path('', views.show, name='show'),
]
