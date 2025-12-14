from django.shortcuts import render
from .models import Announcement
from django.views.generic import ListView, DetailView
# Create your views here.
class PostListView(ListView):
    model = Announcement
    template_name = 'list.html'

class PostDetailView(DetailView):
    model = Announcement
    template_name = 'comments/list.html'
    
def post_list(request):
    return render(request, 'Redit/comments/templates/list.html')
