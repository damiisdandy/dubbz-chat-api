from rest_framework import serializers
from message.models import Message


class MessageSerializer(serializers.ModelSerializer):
    source = serializers.CharField(write_only=True)

    class Meta:
        model = Message
        fields = ['id', 'text', 'source', 'created_at']
