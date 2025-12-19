from django.shortcuts import render
from .models import Announcement
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from django.contrib.auth.mixins import (LoginRequiredMixin, UserPassesTestMixin)
from django.contrib.auth.forms import UserCreationForm
from .forms import PostForm
#from .forms import PostForm
# Create your views here.
class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'
    
class PostListView(ListView):
    model = Announcement
    template_name = 'post_list.html'

class PostDetailView(DetailView):
    model = Announcement
    template_name = 'post_detail.html'
    
class PostCreateView(LoginRequiredMixin, CreateView):
    model = Announcement
    template_name = 'post_create.html'
    form_class = PostForm
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
class PostDeleteView(LoginRequiredMixin, DeleteView):
    model = Announcement
    template_name = 'post_delete.html'
    success_url = reverse_lazy('list')
    
    def test(self):
        task = self.get_object()
        return self.request.user == task.author
    
class PostUpdateView(LoginRequiredMixin, UpdateView, UserPassesTestMixin):
    model = Announcement
    template_name = 'tasks/task_update.html'
