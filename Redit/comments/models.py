from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
import os
# Create your models here.
class Announcement(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("post_detail", kwargs={"pk": self.pk})
    
    @property
    def filename(self):
        return os.path.basename(self.attachment.name)
    
    class Meta:
        ordering = ['-created_at']
    
class Comment(models.Model):
    post = models.ForeignKey(Announcement, on_delete=models.CASCADE, related_name='comments', verbose_name='Завдання')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments', verbose_name="Автор")
    text = models.TextField(verbose_name="Текст коментаря")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"Коментар до {self.post.title}. Автор: {self.author.username} Дата: {self.created_at}"
    
    class Meta:
        ordering = ['created_at']
    