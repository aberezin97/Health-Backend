from django.dispatch import receiver
from django.conf import settings
from django.db.models.signals import post_save
from django.template.loader import render_to_string
from rest_framework.authtoken.models import Token
from user.tokens import account_activation_token
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.core.mail import EmailMessage
from django_rest_passwordreset.signals import reset_password_token_created


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)
        message = render_to_string(
            'activate_email.html',
            {
                'user': instance,
                'domain': settings.FRONTEND_URL,
                'uid': urlsafe_base64_encode(force_bytes(instance.pk)),
                'token': account_activation_token.make_token(instance),
            }
        )
        email = EmailMessage(
            'Health - Активация аккаунта',
            message,
            to=[str(instance.email)]
        )
        email.send()


@receiver(reset_password_token_created)
def password_reset_token_created(sender, instance, reset_password_token, *args, **kwargs):
    message = render_to_string(
        'reset_password_email.html',
        {
            'domain': settings.FRONTEND_URL,
            'token': reset_password_token.key,
        }
    )
    email = EmailMessage(
        'Health - Восстановление пароля',
        message,
        to=[reset_password_token.user.email]
    )
    email.send()
