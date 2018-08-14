from __future__ import absolute_import, division, print_function, unicode_literals

import django_otp.views
from otp_agents.forms import OTPAuthenticationForm, OTPTokenForm


class LoginView(django_otp.views.LoginView):
    """
    This is just like :class:`django_otp.views.LoginView` except that it uses
    our agent-trust-enabled forms.

    """
    otp_authentication_form = OTPAuthenticationForm
    otp_token_form = OTPTokenForm


# Backwards compatibility.
login = LoginView.as_view()
