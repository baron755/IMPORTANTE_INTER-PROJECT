from django.urls import path
from .views import *
urlpatterns = [
    #path('', views.post_list, name='posts'),
    path('', PostListView.as_view(), name='list')
]