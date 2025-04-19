from django.core.mail import send_mail
from django.http import JsonResponse
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.contrib.auth.tokens import default_token_generator
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view

from .models import CustomUser

def send_verification_email(user):
    uid = urlsafe_base64_encode(force_bytes(user.pk))
    token = default_token_generator.make_token(user)

    link = f"http://localhost:8000/api/verify-email/{uid}/{token}/"

    send_mail(
        'Подтверждение регистрации',
        f'Здравствуйте, перейдите по ссылке для подтверждения аккаунта:\n{link}',
        'no-reply@example.com',
        [user.email],
        fail_silently=False,
    )

from rest_framework.response import Response


@api_view(['POST'])
def send_password_reset_email(request):
    email = request.data.get("email", "").strip().lower()

    user = CustomUser.objects.filter(email=email).first()
    if not user:
        return Response({'error': 'Пользователь с таким email не найден'}, status=404)

    uid = urlsafe_base64_encode(force_bytes(user.pk))
    token = default_token_generator.make_token(user)

    link = f"http://localhost:8000/api/password-reset-confirm/{uid}/{token}/"
    send_mail(
        'Reset your password',
        f'Follow the link below:\n{link}',
        'no-reply@example.com',
        [user.email],
        fail_silently=False,
    )
    return Response({"message": "Ссылка на сброс пароля отправлена"}, status=200)
