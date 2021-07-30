from django.urls import path     
from . import views


urlpatterns = [
    path('', views.index),
    path('dos/', views.other_func),
    path('saludar/<nombre>', views.saludar),
    # acá estan las rutas que nos interesan
    path('home/<video>', views.home),
    path('time', views.time),
    path('login', views.login),
]
