.. image:: https://img.shields.io/pypi/v/django-otp-agents?color=blue
   :target: https://pypi.org/project/django-otp-agents/
   :alt: PyPI
.. image:: https://img.shields.io/readthedocs/django-otp-agents
   :target: https://django-otp-agents.readthedocs.io/
   :alt: Documentation
.. image:: https://img.shields.io/badge/github-django--otp--agents-green
   :target: https://github.com/django-otp/django-otp-agents
   :alt: Source

This uses `django-agent-trust`_ to add OTP-based machine authorization to
django-otp.

See `django-otp`_ for more information on the OTP framework.

.. _django-agent-trust: http://pypi.org/project/django-agent-trust
.. _django-otp: http://pypi.org/project/django-otp

.. end-of-doc-intro


Development
-----------

This project is built and managed with `hatch`_. If you don't have hatch, I
recommend installing it with `pipx`_: ``pipx install hatch``.

``pyproject.toml`` defines several useful scripts for development and testing.
The default environment includes all dev and test dependencies for quickly
running tests. The ``test`` environment defines the test matrix for running the
full validation suite. Everything is executed in the context of the Django
project in test/test\_project.

As a quick primer, hatch scripts can be run with ``hatch run [<env>:]<script>``.
To run linters and tests in the default environment, just run
``hatch run check``. This should run tests with your default Python version and
the latest Django. Other scripts include:

* **manage**: Run a management command via the test project. This can be used to
  generate migrations.
* **lint**: Run all linters.
* **fix**: Run all fixers to address linting issues. This may not fix every
  issue reported by lint.
* **test**: Run all tests.
* **check**: Run linters and tests.
* **warn**: Run tests with all warnings enabled. This is especially useful for
  seeing deprecation warnings in new versions of Django.
* **cov**: Run tests and print a code coverage report.

To run the full test matrix, run ``hatch run test:run``. You will need multiple
specific Python versions installed for this.

You can clean up the hatch environments with ``hatch env prune``, for example to
force dependency updates.


.. _hatch: https://hatch.pypa.io/
.. _pipx: https://pypa.github.io/pipx/
