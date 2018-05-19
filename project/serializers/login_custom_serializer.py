# -*- coding: utf-8 -*-
from django.contrib.auth import authenticate
from rest_auth.serializers import LoginSerializer
from rest_framework import exceptions


class LoginSerializerCustom(LoginSerializer):
    def _validate_username(self, username, password):
        user = None
        request = self.context.get('request')

        if username and password:
            user = authenticate(request=request, username=username, password=password)
        else:
            msg = _('Must include "username" and "password".')
            raise exceptions.ValidationError(msg)

        return user

    def _validate_email(self, email, password):
        user = None
        request = self.context.get('request')

        if email and password:
            user = authenticate(request=request, email=email, password=password)
        else:
            msg = _('Must include "username" and "password".')
            raise exceptions.ValidationError(msg)

        return user