# encoding: utf-8
# Created by Jeremy Bowman on Tue Dec  9 13:06:08 EST 2014
# Copyright (c) 2014 Safari Books Online, LLC. All rights reserved.

"""Settings for use when using runserver locally (profiling or just trying out code)"""

from __future__ import unicode_literals

from pinkflamingo.settings.defaults import DATABASES, LOGGING

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.dummy.DummyCache',
    },
}

DATABASES['default']['CONN_MAX_AGE'] = 0  # Disable persistent connections

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

LOGGING['formatters']['simple']['format'] = '%(module)s[%(levelname)s] %(message)s'
LOGGING['handlers']['console'] = {
    'level': 'DEBUG',
    'class': 'logging.StreamHandler',
    'formatter': 'simple'
}
for logger in LOGGING['loggers']:
    LOGGING['loggers'][logger]['handlers'] = ['console']

PASSWORD_HASHERS = (
    'django.contrib.auth.hashers.MD5PasswordHasher',
    'django.contrib.auth.hashers.SHA1PasswordHasher',
)
