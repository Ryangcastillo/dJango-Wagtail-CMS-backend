"""Pytest configuration and fixtures for Debuttend CMS tests."""
from __future__ import annotations

import os
import sys
from pathlib import Path

import pytest

# Add debuttend_cms to Python path
project_root = Path(__file__).parent.parent
debuttend_cms_path = project_root / "debuttend_cms"
if str(debuttend_cms_path) not in sys.path:
    sys.path.insert(0, str(debuttend_cms_path))

# Configure Django settings for pytest
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "debuttend_cms.settings.test")
