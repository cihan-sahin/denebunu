from django.urls import path
from .views import PressContent,PressContentCreateView,PressContentDeleteView,PressContentUpdateView,PressContentDetailView
from . import views

urlpatterns = [
    path('news/new',PressContentCreateView.as_view(),name='news-create'),
    path('news/<int:pk>/update',PressContentUpdateView.as_view(),name='news-update'),
    path('news/<int:pk>/delete',PressContentDeleteView.as_view(),name='news-delete'),
    path('news/<int:pk>/detail',PressContentDetailView.as_view(),name='news-detail'),
]