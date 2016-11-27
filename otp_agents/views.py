from __future__ import absolute_import, division, print_function, unicode_literals

from functools import partial

from django.contrib.auth import BACKEND_SESSION_KEY
from django.contrib.auth.views import login as auth_login

from django_otp import _user_is_anonymous
from otp_agents.forms import OTPAuthenticationForm, OTPTokenForm


def login(request, **kwargs):
    """
    This is just like :func:`django_otp.views.login` except that it uses our
    agent-trust-enabled forms.
    """
    user = request.user

    if _user_is_anonymous(user) or user.is_verified():
        form = OTPAuthenticationForm
    else:
        form = partial(OTPTokenForm, user)

        # A minor hack to make django.contrib.auth.login happy
        user.backend = request.session[BACKEND_SESSION_KEY]

    kwargs['authentication_form'] = form

    return auth_login(request, **kwargs)
