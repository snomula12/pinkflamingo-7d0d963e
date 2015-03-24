# encoding: utf-8
# Created by Jeremy Bowman on Wed Dec  3 15:53:41 EST 2014
# Copyright (c) 2014 Safari Books Online, LLC. All rights reserved.

"""
Support for settings which are dependent on the environment-specific values of
other settings
"""

from __future__ import unicode_literals

import os
import sys

# List of the names of settings which are initially set to functions that
# derive the real value after environment-specific settings have been set.
# Other settings modules add to the list as necessary.
DERIVED_SETTINGS = []

ROOT_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..'))


def derive_settings(settings_module_name):
    """Calculate the real value of each setting listed in DERIVED_SETTINGS"""
    settings = sys.modules[settings_module_name]
    for name in DERIVED_SETTINGS:
        function = getattr(settings, name)
        if callable(function):
            setattr(settings, name, function(settings))
