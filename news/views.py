from django.shortcuts import render
from django.views.generic import DetailView
from admin_panel.models import PressContent,ListView


def home(request):
    context = {
        'title': 'Home',
        'posts': Post.objects.all()
    }
    return render(request,'blog/home.html',context)

# Create your views here.
class NewsDetailView(DetailView):
    model = PressContent

class PressContentListView(ListView):
    model = PressContent
    template_name = 'blog/user_posts.html' # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    paginate_by = 5 
    ordering = ['-date_published']