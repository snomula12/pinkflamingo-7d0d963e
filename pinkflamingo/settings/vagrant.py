# encoding: utf-8
# Created by Jeremy Bowman on Mon Dec  1 10:33:59 EST 2014
# Copyright (c) 2014 Safari Books Online, LLC. All rights reserved.

"""Settings for use in local development environments"""

from __future__ import unicode_literals

from .defaults import *
from .includes.runserver import *

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
    'django.template.loaders.eggs.Loader',
)

STORAGE_PATH = '/mnt/pinkflamingo-vagrant/storage'

DATABASES['default'].update({
    'NAME': 'pinkflamingo',
    'USER': 'pinkflamingo',
    'PASSWORD': 'password',
    'HOST': 'localhost',
    'PORT': '5432',
})

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'simple': {
            'format': '%(module)s[%(levelname)s] %(message)s'
        },
        },
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'console':{
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'simple'
        },
        },
    'loggers': {
        '': {
            'handlers': ['console'],
            'level': 'DEBUG',
            'propagate': False,
            },
        'django.request': {
            'handlers': ['console'],
            'level': 'DEBUG',
            'propagate': False,
            },
        'django.db.backends': {
            'handlers': ['console'],
            'level': 'INFO',
            'propagate': False,
            },
        'django.security.DisallowedHost': {
            'handlers': ['console'],
            'level': 'DEBUG',
            'propagate': False,
            },
        'nose': {
            'handlers': ['console'],
            'level': 'INFO',
            'propagate': False,
            },
        'requests': {
            'handlers': ['console'],
            'propagate': True,
            'level': 'WARNING',
            },
        'suds': {
            'handlers': ['console'],
            'level': 'ERROR',
            'propagate': True,
            },
        'template_timings_panel': {
            'handlers': ['console'],
            'level': 'INFO',
            'propagate': False,
            },
        }
}

# Django Debug Toolbar:
try:
    import debug_toolbar
    DEBUG_TOOLBAR_PATCH_SETTINGS = False
    MIDDLEWARE_CLASSES += ('debug_toolbar.middleware.DebugToolbarMiddleware',)
    INSTALLED_APPS += ('debug_toolbar',)

    DEBUG_TOOLBAR_CONFIG = {
        'SHOW_TOOLBAR_CALLBACK': 'pinkflamingo.should_show_debug_toolbar',
    }
    DEBUG_TOOLBAR_PANELS = [
        'debug_toolbar.panels.versions.VersionsPanel',
        'debug_toolbar.panels.timer.TimerPanel',
        'debug_toolbar.panels.settings.SettingsPanel',
        'debug_toolbar.panels.headers.HeadersPanel',
        'debug_toolbar.panels.request.RequestPanel',
        'debug_toolbar.panels.sql.SQLPanel',
        'debug_toolbar.panels.staticfiles.StaticFilesPanel',
        'debug_toolbar.panels.templates.TemplatesPanel',
        'debug_toolbar.panels.cache.CachePanel',
        'debug_toolbar.panels.signals.SignalsPanel',
        'debug_toolbar.panels.logging.LoggingPanel',
    ]
    try:
        # Haystack panel
        import haystack_panel
        DEBUG_TOOLBAR_PANELS.append('haystack_panel.panel.HaystackDebugPanel')
        INSTALLED_APPS += ('haystack_panel',)
    except ImportError:
        pass
    try:
        # HTML Tidy panel
        # For HTML5 validation:
        #   brew install --HEAD https://raw.github.com/safarijv/tidy-html5/master/tidy.rb
        import debug_toolbar_htmltidy
        DEBUG_TOOLBAR_PANELS.append('debug_toolbar_htmltidy.panels.HTMLTidyDebugPanel')
        INSTALLED_APPS += ('debug_toolbar_htmltidy',)
    except ImportError:
        pass
    try:
        # Template-Timings panel
        import template_timings_panel
        DEBUG_TOOLBAR_PANELS.append('template_timings_panel.panels.TemplateTimings.TemplateTimings')
        INSTALLED_APPS += ('template_timings_panel',)
    except ImportError:
        pass
except ImportError:
    pass

try:
    from .local.dev import *
except ImportError:
    pass

derive_settings(__name__)
