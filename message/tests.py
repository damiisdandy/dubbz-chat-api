from django.test import TestCase, Client
from django.urls import reverse
from rest_framework import status
from message.models import Message
from message.serializers import MessageSerializer
from rest_framework_api_key.models import APIKey

client = Client()


class MessageTestCase(TestCase):
    """Test Messages API"""

    def setUp(self):
        Message.objects.create(text="Hey world", source="10.0.0.1")
        _, key = APIKey.objects.create_key(name="custom API Key")
        self.apiKey = key

    def test_can_create_message(self):
        """Can Create Message Successfully"""
        response = client.post(reverse('Create Message'), {
            "text": "new message",
            "source": "10.0.0.1"
        })
        new_message_exists = Message.objects.filter(
            text="new message").exists()

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(new_message_exists)

    def test_can_fetch_all_messages(self):
        """Can Fetch all Messages"""
        response = client.get(reverse('Fetch all Message'))
        all_messages = Message.objects.all()
        serializer = MessageSerializer(all_messages, many=True)

        self.assertEqual(response.data["data"], serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_can_delete_message(self):
        """Can Delete Message"""
        header = {'HTTP_X_API_KEY': self.apiKey}
        response = client.delete(reverse('Delete Message', kwargs={
            "message_id": 1
        }), **header)
        new_message_exists = Message.objects.filter(
            id=1).exists()

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(new_message_exists)

    def test_can_delete_all_messages(self):
        """Can Delete All Messages"""
        header = {'HTTP_X_API_KEY': self.apiKey}
        response = client.delete(reverse('Delete All'), **header)
        all_messages_count = Message.objects.count()

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(all_messages_count, 0)
