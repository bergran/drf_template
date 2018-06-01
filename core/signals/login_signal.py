# -*- coding: utf-8 -*-
from django.contrib.auth.models import User
from django.core.cache import cache
from django.conf import settings


def prefix_login_attempts(username):
    return 'user_attempts:{}'.format(username)


def login_success(sender, user, request, **kwargs):
    cache.set(prefix_login_attempts(user.username), 0, 0)


def login_fail(sender, credentials, request):
    username = credentials.get('username')
    user_prefix = prefix_login_attempts(username)
    attempts = cache.get(user_prefix, 0) + 1

    cache.set(
        prefix_login_attempts(user_prefix), attempts, 300
    )

    if attempts > settings.LOGIN_ATTEMPTS:
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            return

        user.is_active = False
