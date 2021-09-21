from django.shortcuts import render
from django.views.generic import DetailView
from admin_panel.models import PressContent
from django.db.models.functions import TruncYear


def home(request):
    context = {
        'title': 'Home',
        'news': PressContent.objects.order_by('-date'),
    }
    return render(request,'news/home.html',context)

# Create your views here.
class NewsDetailView(DetailView):
    model = PressContent
