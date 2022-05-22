from django.urls import path
from . import views
urlpatterns = [
    path('', views.index),
    path('home',views.home),
    path('player/',views.player),
    path('team/',views.team,)
]