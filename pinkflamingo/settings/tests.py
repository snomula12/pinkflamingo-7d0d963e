# encoding: utf-8
# Created by Jeremy Bowman on Mon Dec  1 10:45:59 EST 2014
# Copyright (c) 2014 Safari Books Online, LLC. All rights reserved.

"""Settings common to all test runs"""

from __future__ import unicode_literals

from .defaults import *

LOG_DIR = os.path.join(ROOT_PATH, 'log')

# nose installs handlers that only show output for failed tests, but they
# can omit errors in setup and teardown; log everything to file also
if not os.path.exists(LOG_DIR):
    os.makedirs(LOG_DIR)
TESTS_LOG_FILE = os.path.join(LOG_DIR, 'tests.log')

# Log file for tests should only contain the latest run
with open(TESTS_LOG_FILE, 'w') as f:
    f.write('')

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.dummy.DummyCache',
        'LOCATION': 'pinkflamingo-test-unique-snowflake'
    },
    'test_cache': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
        'LOCATION': 'twas-brillig'
    },
}

DATABASES['default']['CONN_MAX_AGE'] = 0  # Disable persistent connections

INSTALLED_APPS += (
    'django_nose',
)

LOGGING['disable_existing_loggers'] = True
LOGGING['handlers']['file'] = {
    'class': 'logging.FileHandler',
    'filename': TESTS_LOG_FILE,
    'formatter': 'simple',
    'level': 'DEBUG',
}
for logger in LOGGING['loggers']:
    LOGGING['loggers'][logger]['handlers'] = ['file']

NOSE_ARGS = [
    '--cover-erase',
    '--cover-package=pinkflamingo,api',
    '--logging-clear-handlers',
    '--with-coverage',
    '--verbose',
]

PASSWORD_HASHERS = (
    'django.contrib.auth.hashers.MD5PasswordHasher',
    'django.contrib.auth.hashers.SHA1PasswordHasher',
)

# Set the test runner
TEST_RUNNER = 'django_nose.NoseTestSuiteRunner'

TESTING = True

# Developers should always have a pinkflamingo/settings/local/tests.py file.  Copy it
# from pinkflamingo/settings/local/tests.py.example and customize.
# If you need to locally override things (like NOSE_ARGS), add them to the local test settings file
try:
    from .local.tests import *
except ImportError:
    print u"FYI: You have no pinkflamingo/settings/local/tests.py, but you should!"
    pass

derive_settings(__name__)
