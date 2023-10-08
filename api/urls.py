from django.urls import path
from api.views.user_views import UserRegisterView, CustomObtainAuthToken
from api.views.message_views import generate_telegram_token, send_message, get_messages, get_user_messages


urlpatterns = [
    path('register/', UserRegisterView.as_view(), name='register'),
    path('generate_telegram_token/', generate_telegram_token, name='generate_telegram_token'),
    path('send_message/', send_message, name='send_message'),
    path('get_messages/', get_messages, name='get_messages'),
    path('login/', CustomObtainAuthToken.as_view(), name='login'),
    path('get_user_messages/', get_user_messages, name='get_user_messages')
]
