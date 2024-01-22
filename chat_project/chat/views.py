# chat/views.py

from django.shortcuts import render
from rest_framework import generics
from .models import Message
from .serializers import MessageSerializer

class MessageListView(generics.ListCreateAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer

def index(request):
    return render(request, 'index.html')
