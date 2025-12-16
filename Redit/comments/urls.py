from django.urls import path
from .views import *
urlpatterns = [
    #path('', post_list, name='posts'),
    path('', PostDeleteView.as_view(), name='post_delete')
]

