from django.shortcuts import render
from .models import Announcement
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from django.contrib.auth.mixins import (LoginRequiredMixin, UserPassesTestMixin)
from django.contrib.auth.forms import UserCreationForm
from .forms import PostForm, CommentForm
from django.views.generic.edit import FormMixin
# Create your views here.
class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'
    
class PostListView(LoginRequiredMixin, ListView):
    model = Announcement
    template_name = 'post_list.html'
    context_object_name = 'posts'
    paginate_by = 5
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class PostDetailView(LoginRequiredMixin, DetailView, FormMixin):
    model = Announcement
    template_name = 'post_detail.html'
    form_class = CommentForm
    
    def get_success_url(self):
        return reverse('post_detail', kwargs={'pk': self.object.pk})
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comment_form'] = self.get_form()
        context['comments'] = self.object.comments.all()
        return context
    
    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid(form):
            return self.form_valid(form)
        else:
            return self.form_invalid(form)
    
    def form_valid(self, form):
        comment = form.save(commit=False)
        comment.post = self.object
        comment.author = self.request.user
        comment.save()
        return super().form_valid(form)
    
class PostCreateView(LoginRequiredMixin, CreateView):
    model = Announcement
    template_name = 'post_create.html'
    form_class = PostForm
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
class PostDeleteView(LoginRequiredMixin, DeleteView, UserPassesTestMixin):
    model = Announcement
    template_name = 'post_delete.html'
    success_url = reverse_lazy('post_list')
    
    def test(self):
        task = self.get_object()
        return self.request.user == task.author
    
class PostUpdateView(LoginRequiredMixin, UpdateView, UserPassesTestMixin):
    model = Announcement
    template_name = 'task_update.html'
    form_class = PostForm
    
    def test(self):
        task = self.get_object()
        return self.request.user == task.author