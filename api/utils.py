from django.core.signing import Signer

#проверка при использовании токена
def verify_telegram_token(user, received_token):
    signer = Signer()
    try:
        original_token = signer.unsign(received_token)
        return original_token == user.telegram_token
    except:
        return False
