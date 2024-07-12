from django.urls import path
from . import views

urlpatterns = [
    path('', views.beranda, name='beranda'),
    path('tentang/', views.tentang, name='tentang'),
    path('identifikasi/', views.identifikasi, name='identifikasi'),
]