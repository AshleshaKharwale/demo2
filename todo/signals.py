from django.contrib.auth.signals import (
        user_logged_in, user_logged_out, user_login_failed
)
from django.contrib.auth.models import User
from django.dispatch import receiver

from home.views import LogoutView


@receiver(user_logged_in, sender=User)
def login_signal(sender, request, user, *args, **kwargs):
    print("-------------------" * 7)
    print("Log in Signal")
    print("sender:", sender)
    print("request:", request)
    print("user:", user)
    print("User logged-in successfully!")
    print("-------------------" * 7)


# manually connecting signal to sender
# user_logged_in.connect(login_signal, sender=User)


@receiver(user_logged_out, sender=User)
def logout_signal(sender, request, user, *args, **kwargs):
    print("-------------------" * 7)
    print("Log out Signal")
    print("sender:", sender)
    print("request:", request)
    print("user:", user)
    print("User logged-out successfully!")
    print("-------------------" * 7)


@receiver(user_login_failed)
def login_fail_signal(sender, request, credentials, *args, **kwargs):
    print("-------------------" * 7)
    print("Log in fail Signal")
    print("sender:", sender)
    print("request:", request)
    print("credentials:", credentials)
    print("User could not log-in!!!")
    print("-------------------" * 7)

