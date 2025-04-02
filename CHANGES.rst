Unreleased - Tooling and Django 5.2
--------------------------------------------------------------------------------

Update test matrix for Django 5.2. No substantive changes.

This project is now managed with `hatch`_, which replaces setuptools, pipenv,
and tox. Users of the package should not be impacted. Developers can refer to
the readme for details. If you're packaging this project from source, I suggest
relying on pip's isolated builds rather than using hatch directly.

.. _hatch: https://hatch.pypa.io/


v1.0.1 - November 29, 2021 - Forward compatibility
--------------------------------------------------------------------------------

Default to AutoField to avoid spurious migrations.


v1.0.0 - August 13, 2020 - Drop unsupported Python and Django versions
--------------------------------------------------------------------------------

- Now supports Python>=3.5 and Django>=2.2.


v0.5.1 - August 26, 2019 - Housekeeping
--------------------------------------------------------------------------------

Build, test, and documentation cleanup.


v0.5.0 - August 14, 2018 - Django 2.1 support
--------------------------------------------------------------------------------

- Remove dependencies on old non-class login views.

- Drop support for Django < 1.11.


v0.3.0 - July 19, 2017 - Update support matrix
--------------------------------------------------------------------------------

- Drop support for versions of Django that are past EOL.


v0.2.6 - April 2, 2017 - Django 1.11 compatibility
--------------------------------------------------------------------------------

- Minor test fix for Django 1.11.


v0.2.5 - November 27, 2016 - Forward compatibility for Django 2.0
--------------------------------------------------------------------------------

- Treat :attr:`~django.contrib.auth.models.User.is_authenticated` and
  :attr:`~django.contrib.auth.models.User.is_anonymous` as properties in Django
  1.10 and later.

- Add explict on_delete behavior for all foreign keys.


v0.2.4 - January 10, 2016 - Python 3 cleanup
--------------------------------------------------------------------------------

- All modules include all four Python 3 __future__ imports for consistency.

- Migrations no longer have byte strings in them.


v0.2.3 - November 16, 2015 - admin
--------------------------------------------------------------------------------

- Added :class:`~otp_agents.admin.TrustedAgentAdminSite`, which is an admin site
  that accepts either a verified user or a trusted agent.


v0.2.2 - October 11, 2015 - Django 1.8
--------------------------------------------------------------------------------

- Stop importing models into the root of the package.

- General cleanup and compatibility with Django 1.9a1.


v0.2.1 - April 3, 2015 - Django 1.8
--------------------------------------------------------------------------------

- Add support for the new app registry, when available.

- Add Django 1.8 to the test matrix and fix a few test bugs.


v0.2.0 - November 10, 2013 - Django 1.6
--------------------------------------------------------------------------------

- Now supports Django 1.4 to 1.6 on Python 2.6, 2.7, 3.2, and 3.3. This is the
  first release for Python 3.


v0.1.4 -- August 20, 2013 - Fix in otp_required
--------------------------------------------------------------------------------

- :func:`~otp_agents.decorators.otp_required` no longer ignores
  ``if_configured`` when ``accept_trusted_agent`` is ``True``. The default
  behavior for ``login_url`` is also now more explicit.


v0.1.3 -- July 3, 2013 - Decorator improvement
--------------------------------------------------------------------------------

- Add if_configured argument to :func:`~otp_agents.decorators.otp_required`.


v0.1.2 - May 9, 2013 - Unit test improvements
--------------------------------------------------------------------------------

- Major unit test cleanup. Tests should pass or be skipped under all supported
  versions of Django, with or without custom users and timezone support.


v0.1.1 - October 8, 2012 - Django < 1.4
--------------------------------------------------------------------------------

- As a convenience, all unit tests are skipped in Django < 1.4.


v0.1.0 - August 20, 2012 - Initial Release
--------------------------------------------------------------------------------

Initial release.


.. vim: ft=rst nospell tw=80
