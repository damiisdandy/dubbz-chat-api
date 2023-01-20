from django.urls import path
from message.views import create, get_messages, delete_message, delete_all, generate_api_key

urlpatterns = [
    path('create', create, name="Create Message"),
    path('all', get_messages, name="Fetch all Message"),
    path('delete/<int:message_id>', delete_message, name="Delete Message"),
    path('delete/all', delete_all, name="Delete All"),
    path('api-key/generate', generate_api_key, name="Generate API Key")
]
