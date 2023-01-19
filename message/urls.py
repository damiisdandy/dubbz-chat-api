from django.urls import path
from message.views import create, get_messages

urlpatterns = [
    path('create', create, name="Create Message"),
    path('all', get_messages, name="Fetch all Message"),
]
