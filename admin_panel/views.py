from django.shortcuts import render,get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.views.generic import CreateView, UpdateView, DeleteView,DetailView
from .models import PressContent



def admin_panel(request):
    context = {
        'title': 'Admin',
        'news': PressContent.objects.all()
    }
    return render(request,'news/home.html',context)

class PressContentDetailView(DetailView):
    model = PressContent
class PressContentCreateView(LoginRequiredMixin,CreateView):
    model = PressContent
    fields = ['label','url','date']
    template_name= 'admin_panel/presscontent_form.html'


class PressContentUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = PressContent
    fields = ['label','url','date']

    def test_func(self):
        post = self.get_object()
        return True
    


class PressContentDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = PressContent
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        return True

