from django.urls import path
from .views import *
urlpatterns = [
    path('signup/', SignUpView.as_view(), name="signup"),
    path('', PostListView.as_view(), name='post_list'),
    path('post/new/', PostCreateView.as_view(), name="post_create"),
    path('task/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    path('task/<int:pk>/delete', PostDeleteView.as_view(), name="post_delete"),
    path('task/<int:pk>/update', PostUpdateView.as_view(), name="post_update"),
]

