# chat/urls.py

from django.urls import path
from .views import MessageListView, index

urlpatterns = [
    path('messages/', MessageListView.as_view(), name='message-list'),
    path('', index, name='index'),
]
