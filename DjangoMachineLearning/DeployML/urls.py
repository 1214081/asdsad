from django.urls import path
from .import views

urlpatterns = [
    path('', views.Home, name='Home'),
    path('visualisasi1/', views.Visualisasi1, name='Visualisasi1'),
    path('visualisasi2/', views.Visualisasi2, name='Visualisasi2')
]
