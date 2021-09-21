from django.shortcuts import render
from django.views.generic import DetailView
from admin_panel.models import PressContent


def home(request):
    context = {
        'title': 'Home',
        'news': PressContent.objects.all()
    }
    return render(request,'news/home.html',context)

# Create your views here.
class NewsDetailView(DetailView):
    model = PressContent
