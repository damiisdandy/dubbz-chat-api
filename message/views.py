from message.serializers import MessageSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework import status
from message.models import Message
from django.shortcuts import get_object_or_404
from rest_framework_api_key.permissions import HasAPIKey
from rest_framework_api_key.models import APIKey


@api_view(['POST'])
def create(request):
    serializer = MessageSerializer(data=request.data)
    if serializer.is_valid():
        message = serializer.save()
        return Response({
            "status": True,
            "message": "Message Created",
            "data": MessageSerializer(message).data
        }, status=status.HTTP_201_CREATED)
    return Response({
        "status": False,
        "message": "Problem creating message",
        "data": None,
        "cause": serializer.errors
    })


@api_view(['GET'])
def get_messages(request):
    try:
        messages = Message.objects.all().order_by("-created_at")
        return Response({
            "status": True,
            "message": "Fetched all messages",
            "data": MessageSerializer(messages, many=True).data
        }, status=status.HTTP_200_OK)
    except:
        return Response({
            "status": True,
            "message": "Problem fetching messages",
            "data": None
        }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['DELETE'])
@permission_classes([HasAPIKey])
def delete_message(request, message_id):
    try:
        message = get_object_or_404(Message, id=message_id)
        message.delete()
        return Response({
            "status": True,
            "message": "Message deleted",
            "data": MessageSerializer(message).data
        }, status=status.HTTP_204_NO_CONTENT)
    except:
        return Response({
            "status": True,
            "message": "Problem deleting message",
            "data": None
        }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['DELETE'])
@permission_classes([HasAPIKey])
def delete_all(request):
    try:
        Message.objects.all().delete()
        return Response({
            "status": True,
            "message": "All Messages deleted",
            "data": None
        }, status=status.HTTP_204_NO_CONTENT)
    except:
        return Response({
            "status": True,
            "message": "Problem deleting messages",
            "data": None
        }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


# exposed publically for testing purposes#
# for a real life scenario this will be backed by authentication
# to attach API key to user, or for only `is_admin` to have the ablility to generate
@api_view(['GET'])
def generate_api_key(request):
    _, key = APIKey.objects.create_key(name="custom API Key")
    return Response({
        "status": True,
        "message": "Api Key Generated",
        "data": {
            "api_key": key,
        }
    }, status=status.HTTP_200_OK)
