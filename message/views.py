from message.serializers import MessageSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from message.models import Message


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
        "cause": serializer.error_messages
    })


@api_view(['GET'])
def get_messages(request):
    try:
        messages = Message.objects.all()
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
