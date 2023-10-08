import logging
import secrets

from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from telegram import Bot

from api.models import Message
from api.serializers.message_serializers import MessageSerializer
from config import settings
from django.core.signing import Signer
bot = Bot(token=settings.TELEGRAM_BOT_TOKEN)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def generate_telegram_token(request):
    signer = Signer()
    user = request.user

    # Сгенерируем токен и подпишем его
    original_token = secrets.token_hex(16)
    signed_token = signer.sign(original_token)

    user.telegram_token = signed_token
    user.save()
    return Response({'telegram_token': signed_token})


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def send_message(request):
    message_text = request.data.get('text')
    user = request.user

    message = Message(user=user, text=message_text)
    message.save()

    try:
        bot.send_message(chat_id=user.telegram_chat_id, text=f"{user.username}, я получил от тебя сообщение:\n{message_text}")
    except Exception as e:
        logging.error(f"Error sending Telegram message: {e}")
        return Response({"error": "Failed to send Telegram message"}, status=500)

    return Response({'status': 'success'})


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_user_messages(request):
    messages = Message.objects.filter(user=request.user)
    serializer = MessageSerializer(messages, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_messages(request):
    messages = Message.objects.filter(user=request.user).order_by('-date_sent')
    serializer = MessageSerializer(messages, many=True)
    return Response(serializer.data)
