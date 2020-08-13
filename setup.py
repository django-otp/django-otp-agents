#!/usr/bin/env python

from setuptools import setup


setup(
    name='django-otp-agents',
    version='1.0.0',
    description="Integration of django-otp and django-agent-trust.",
    author="Peter Sagerson",
    author_email='psagers@ignorare.net',
    url='https://github.com/django-otp/django-otp-agents',
    project_urls={
        "Documentation": 'https://django-otp-agents.readthedocs.io/',
        "Source": 'https://github.com/django-otp/django-otp-agents',
    },
    license='BSD',
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3 :: Only",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Topic :: Security",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Framework :: Django",
    ],

    package_dir={'': 'src'},
    packages=[
        'otp_agents',
        'otp_agents.test',
    ],

    install_requires=[
        'django-otp >= 1.0.0',
        'django-agent-trust >= 1.0.0',
    ],
)
