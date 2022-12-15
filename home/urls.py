from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="home"),
    path('about/', views.about, name="about"),
    path('policy/', views.privacy, name="privacy_policy"),
    path('404/', handler404),
]

handler404 = 'home.views.handler404'
