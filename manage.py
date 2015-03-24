#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":
    parent_dir = os.path.abspath(os.path.dirname(__file__))
    if 'test' in sys.argv:
        default_settings = 'pinkflamingo.settings.tests'
    elif 'pinkflamingo-prod' in parent_dir:
        default_settings = 'pinkflamingo.settings.prod'
    elif 'pinkflamingo-vagrant' in parent_dir:
        default_settings = 'pinkflamingo.settings.vagrant'
    else:
        default_settings = 'pinkflamingo.settings.dev'
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", default_settings)

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
