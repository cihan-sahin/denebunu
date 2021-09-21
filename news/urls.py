from django.urls import path
from .views import NewsDetailView 
from . import views

urlpatterns = [
    path('', views.home, name='news-home'),
    path('news/<int:pk>', NewsDetailView.as_view(), name='news-detail'),  
]