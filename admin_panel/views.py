from django.shortcuts import render,get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.views.generic import CreateView, UpdateView, DeleteView
from .models import PressContent



def admin_panel(request):
    context = {
        'title': 'Admin',
        'news': PressContent.objects.all()
    }
    return render(request,'news/home.html',context)

class PressContentCreateView(LoginRequiredMixin,CreateView):
    model = PressContent
    fields = ['label','url','date_published']


class PressContentUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = PressContent
    fields = ['label','url','date_published']


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = PressContent
    success_url = '/'

