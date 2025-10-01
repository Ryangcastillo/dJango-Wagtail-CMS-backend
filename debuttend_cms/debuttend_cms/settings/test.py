"""Test settings for Debuttend CMS.

This settings file uses SQLite for testing instead of PostgreSQL.
"""
from __future__ import annotations

from .dev import *  # noqa: F401, F403

# Override database settings for testing
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": ":memory:",
    }
}

# Disable password validation for faster tests
AUTH_PASSWORD_VALIDATORS = []

# Use a simple password hasher for faster tests
PASSWORD_HASHERS = [
    "django.contrib.auth.hashers.MD5PasswordHasher",
]
