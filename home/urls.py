from django.conf.urls import handler404, handler500
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="home"),
    path('about/', views.about, name="about"),
    path('policy/', views.privacy, name="privacy_policy"),
]

handler404 = 'home.views.handler404'
handler500 = 'home.views.handler500'
